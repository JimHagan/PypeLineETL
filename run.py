from __future__ import absolute_import

import optparse
import sys



from config import dimension_configs, fact_configs, _source_conn, _output_conn
from etl import run_dimension_etl, run_fact_etl,\
    load_cached_dimensions, get_etl_logger, delete_existing_dimensions_and_facts
from tests import test_dimension_source_queries

logger = get_etl_logger()

def main(test_dimension_source, run_dimensions,
         run_facts, delete_existing_tables):
    if delete_existing_tables:
        delete_existing_dimensions_and_facts(_output_conn)

    if test_dimension_source:
        try:
            logger.info("Testing dimension queries")
            test_dimension_source_queries()
            logger.info("No exceptions.")
        except Exception as e:
            logger.error("Exception while testing dimension source queries!")
            raise e
    if run_dimensions:
        for d in dimension_configs:
            if d["etl_active"]:
                 run_dimension_etl(pygram_dimension_factory=d["dimension_handler"],
                                  source_conn=_source_conn,
                                  output_conn=_output_conn,
                                  source_sql=d["source_sql"],
                                  create_sql=d["create_sql"])

    if run_facts:
        cached_dimensions = load_cached_dimensions(_output_conn)
        for f in fact_configs:
            if f["etl_active"]:
                run_fact_etl(pygram_fact_factory=f["fact_handler"],
                             source_conn=_source_conn,
                             output_conn=_output_conn,
                             source_sql=f["source_sql"],
                             create_sql=f["create_sql"],
                             dimensions=cached_dimensions)

    return 0


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('--test_dimension_source', action="store_true",
                      default=True,
                      help="Tests the dimensions source SQL queries"
                           " (read-only)")

    parser.add_option('--run_dimensions', action="store_true",
                      default=False, help="Run all active dimension ETLs")

    parser.add_option('--run_facts', action="store_true",
                      default=False, help="Run all active fact ETLs")

    parser.add_option('--delete_existing_tables',
                      action="store_true",
                      default=False, help="Delete all existing dimension and"
                                          " fact tables")

    options, args = parser.parse_args()
    sys.exit(main(options.test_dimension_source,
                  options.run_dimensions,
                  options.run_facts,
                  options.delete_existing_tables))
