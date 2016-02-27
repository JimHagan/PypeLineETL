from datetime import datetime
import logging
import os
import pytz
import sys
import _mysql_exceptions

import pygrametl
from pygrametl.tables import CachedDimension

import csv
import dwexcept

from config import ETL_LOG_HOME, dimension_configs, fact_configs

# earliest date to which we'll attribute product creation.  Using noon UTC
# to ensure that any products adjusted to this date will share the same row
# for the Date and Flashnotes_Date FK values
MIN_DATE = pytz.utc.localize(datetime(2012,1,1,12,0))

if not os.path.exists(ETL_LOG_HOME):
    os.makedirs(ETL_LOG_HOME)
logging.basicConfig(filename=os.path.join(ETL_LOG_HOME, "run.log"),
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def get_etl_logger():
    return logger

def add_foreign_keys(row, keyrefs, dimensions):
    for keyref in keyrefs:
        dim_name, dim_lookup, row_field = get_lookup_args(keyref)
        if 'date' in dim_name:
            pass
        else:
            try:
                row[keyref] = dimensions[dim_name].lookup(row, {dim_lookup: row_field})
            except KeyError:
                pass
                #TODO: implement this dimension
                #logger.warn("TODO: dimension '{0}' not found".format(keyref))
    return row


def get_lookup_args(keyref):
    dim_name = keyref.replace('_fk', '')
    if dim_name in ('seller', 'buyer'):
        dim_name = 'user'
    elif dim_name in ('seller_disability_program', 'buyer_disability_program'):
        dim_name = 'disability_program'
    dim_lookup = '{0}_id'.format(dim_name)
    row_field = keyref.replace('_fk', '_id')
    return dim_name, dim_lookup, row_field


def add_date_foreign_keys(row, timestamp_field):
    dt_utc = ensure_minimum_date(pytz.utc.localize(row[timestamp_field]))
    dt_et = dt_utc.astimezone(pytz.timezone('US/Eastern'))
    row['date_fk'] = datetime.strftime(dt_utc, '%Y%m%d')
    row['flashnotes_date_fk'] = datetime.strftime(dt_et, '%Y%m%d')
    return row


def ensure_minimum_date(dt):
    if dt.year < 2012:
        return MIN_DATE
    return dt


def load_cached_dimensions(output_conn):
    pygram_outputconn = pygrametl.ConnectionWrapper(connection=output_conn)
    ret = dict()
    ret['product'] = CachedDimension(
        name='product_dim',
        key='id',
        attributes=['name',],
        lookupatts=['product_id'],
        prefill=True)
    ret['user'] = CachedDimension(
        name='user_dim',
        key='id',
        attributes=['username',],
        lookupatts=['user_id'],
        prefill=True)
    ret['school'] = CachedDimension(
        name='school_dim',
        key='id',
        attributes=['name',],
        lookupatts=['school_id'],
        prefill=True)
    ret['course'] = CachedDimension(
        name='course_dim',
        key='id',
        attributes=['name',],
        lookupatts=['course_id'],
        prefill=True)
    ret['disability_program'] = CachedDimension(
        name='disability_program_dim',
        key='id',
        attributes=['name',],
        lookupatts=['disability_program_id'],
        prefill=True)
    return ret


def delete_existing_dimensions_and_facts(warehouse_connection):
    cursor = warehouse_connection.cursor()
    fact_tables = [cfg["fact_handler"]["name"] for cfg in fact_configs]
    dimension_tables = [cfg["dimension_handler"]["name"] for cfg in dimension_configs]

    for tbl in (fact_tables + dimension_tables):
        logger.info("Dropping table %s", tbl)
        try:
            cursor.execute("drop table %s" % tbl)
        except Exception as e:
            if "Unknown table" in str(e):
                logger.info("Table doesn't exist")
            else:
                raise e


def run_dimension_etl(pygram_dimension_factory, source_sql,
                      source_conn, output_conn,
                      create_sql="", create_if_needed=True,
                      fail_if_table_exists=True):
    """
    This function can be used in any kind of workflow (for example in a celery
    task) or in a simple main program.
    """

    # This ConnectionWrapper will be set as default and is then implicitly used.
    # A reference to the wrapper is saved to allow for easy access of it later
    pygram_outputconn = pygrametl.ConnectionWrapper(connection=output_conn)

    # Let's figure out if this table exists
    dw_table_exists = True
    table_name = pygram_dimension_factory["name"]
    cursor = output_conn.cursor()
    logger.info("Processing dimension '%s'" % table_name)
    try:
        cursor.execute("desc %s" % table_name)
        if fail_if_table_exists:
            raise dwexcept.DataWarehouseTableAlreadyExists("Table %s already exists.  Use delete_existing_tables to clean the warehouse." % table_name)
        else:
            logger.warn("ETL for %s will be inserting data into an existing table", table_name)
    except _mysql_exceptions.ProgrammingError as e:
        if "DOESN'T EXIST" in str(e).upper():
            dw_table_exists = False
        else: # Some other anomaly
            raise e
    except Exception as e:
        raise e

    if not dw_table_exists:
        logger.info("Creating table %s.", table_name)
        result = cursor.execute(create_sql)
        logger.info("Table %s created.", table_name)

    logger.info("Executing source query for dimension %s", table_name)
    try:
        pygram_dim_class = pygram_dimension_factory["class"]
        pygram_dim_object = pygram_dim_class(
            name=pygram_dimension_factory["name"],
            key=pygram_dimension_factory["key"],
            attributes=pygram_dimension_factory["attributes"],
            lookupatts=pygram_dimension_factory["lookupatts"])
        if source_sql == 'CSV':
            try:
                filepath = os.path.join(
                    os.path.dirname(__file__),
                    'csv_source',
                    '{0}.csv'.format(
                        pygram_dimension_factory["name"]))
                source_cursor = csv.DictReader(open(filepath, 'rb'))
            except IOError as e:
                raise e
        else:
            source_cursor = source_conn.cursor()
            source_cursor.execute(source_sql)

        logger.info("Loading data")
        start_time = datetime.utcnow()
        row_count = 0
        for row in source_cursor:
            row_count += 1
            pygram_dim_object.insert(row)
        end_time = datetime.utcnow()
        logger.info("Loaded %d rows into table %s (elapsed time: %s)",
                    row_count, table_name, end_time - start_time)

        output_conn.commit()
        return row_count
    except Exception as e:
        raise e


def run_fact_etl(pygram_fact_factory, source_sql,
                      source_conn, output_conn,
                      create_sql="", create_if_needed=True,
                      drop_and_replace=True, dimensions={}):

    # This ConnectionWrapper will be set as default and is then implicitly used.
    # A reference to the wrapper is saved to allow for easy access of it later
    pygram_outputconn = pygrametl.ConnectionWrapper(connection=output_conn)

    # Let's figure out if this table exists
    dw_table_exists = True
    table_name = pygram_fact_factory["name"]
    cursor = output_conn.cursor()
    try:
        logger.info("Processing fact %s" % table_name)
        results = cursor.execute("desc %s" % table_name)
        if drop_and_replace:
            logger.info("Dropping table %s", table_name)
            cursor.execute("drop table %s" % table_name)
            logger.info("Dropped table %s", table_name)
            dw_table_exists = False
        else:
            raise dwexcept.DataWarehouseTableAlreadyExists("Table %s already exists.  "
                                                  "Run with drop_and_replace "
                                                  "to=True to automatically "
                                                  "refresh." % table_name)
    except _mysql_exceptions.ProgrammingError as e:
        if "DOESN'T EXIST" in str(e).upper():
            dw_table_exists = False
            logger.info("Table %s does not exist in data warehouse.",
                        table_name)
            if (create_if_needed):
                logger.info("Table will be initialized")
            else:
                raise dwexcept.DataWarehouseTableDoesNotExist("Table %s doesn't exist."
                                                      "  Run with create_if_"
                                                      "needed=True to "
                                                      "automatically generate."
                                                      % table_name)
        else:
            raise e
    except Exception as e:
        raise e

    if not dw_table_exists:
        logger.info("Creating table %s.", table_name)
        result = cursor.execute(create_sql)
        logger.info("Table %s created.", table_name)

    logger.info("Executing source query for fact table %s" % table_name)
    try:
        pygram_fact_class = pygram_fact_factory["class"]
        pygram_fact_object = pygram_fact_class(
            name=pygram_fact_factory["name"],
            measures=pygram_fact_factory["measures"],
            keyrefs=pygram_fact_factory["keyrefs"])
        source_cursor = source_conn.cursor()
        source_cursor.execute(source_sql)
        logger.info("Loading data")
        start_time = datetime.utcnow()
        row_count = 0
        for row in source_cursor:
            row_count += 1
            row = add_foreign_keys(
                row, getattr(pygram_fact_object, 'keyrefs', []), dimensions)
            row = add_date_foreign_keys(
                row, pygram_fact_factory['timestamp_field'])
            pygram_fact_object.insert(row)
        end_time = datetime.utcnow()
        logger.info("Loaded %d rows into table %s (elapsed time: %s)",
                    row_count, table_name, end_time - start_time)

        output_conn.commit()
        return row_count
    except Exception as e:
        import traceback
        traceback.print_tb(sys.exc_info())
        raise e

