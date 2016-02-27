"""
This module is the top level configuration for the flashnotes ETL process.
"""
import os
import MySQLdb
from MySQLdb.cursors import DictCursor
from sql.sources import QUERIES as SOURCE_QUERIES
from sql.creates import QUERIES as CREATE_QUERIES
import dimensions
import facts


ETL_LOG_HOME = "./etl-log"

_test_output_conn = MySQLdb.connect(host='127.0.0.1', db='test', user='', passwd='')

_test_source_conn = MySQLdb.connect(host='127.0.0.1', db='redsprite',
                                    user='redsprite', passwd='redsprite',
                                    cursorclass=DictCursor)

_output_conn = MySQLdb.connect(host=os.environ.get("ETL_OUTPUT_HOST"),
                               db=os.environ.get("ETL_OUTPUT_DB"),
                               user=os.environ.get("ETL_OUTPUT_USER"),
                               passwd=os.environ.get("ETL_OUTPUT_PWD"))  # Change for production

_source_conn = MySQLdb.connect(host=os.environ.get("ETL_SOURCE_HOST"),
                               db=os.environ.get("ETL_SOURCE_DB"),
                               user=os.environ.get("ETL_SOURCE_USER"),
                               passwd=os.environ.get("ETL_SOURCE_PWD"),
                               cursorclass=DictCursor)

dimension_configs = [
    # Validated (quick)
    {"name": "product",
     "source_sql": SOURCE_QUERIES["PRODUCT"],
     "create_sql": CREATE_QUERIES["PRODUCT"],
     "dimension_handler": dimensions.pygram_product_dimension_factory,
     "etl_active": True},

    # Validated (quick)
    {"name": "user",
     "source_sql": SOURCE_QUERIES["USER"],
     "create_sql": CREATE_QUERIES["USER"],
     "dimension_handler": dimensions.pygram_user_dimension_factory,
     "etl_active": True},

    # Validated (quick)
    {"name": "course",
     "source_sql": SOURCE_QUERIES["COURSE"],
     "create_sql": CREATE_QUERIES["COURSE"],
     "dimension_handler": dimensions.pygram_course_dimension_factory,
     "etl_active": True},

    {"name": "date",
     "source_sql": SOURCE_QUERIES["DATE"],
     "create_sql": CREATE_QUERIES["DATE"],
     "dimension_handler": dimensions.pygram_date_dimension_factory,
     "etl_active": True},

    # Validated (quick)
    {"name": "school",
     "source_sql": SOURCE_QUERIES["SCHOOL"],
     "create_sql": CREATE_QUERIES["SCHOOL"],
     "dimension_handler": dimensions.pygram_school_dimension_factory,
     "etl_active": True},

    {"name": "payment_source",
     "source_sql": SOURCE_QUERIES["PAYMENT_SOURCE"],
     "create_sql": CREATE_QUERIES["PAYMENT_SOURCE"],
     "dimension_handler": dimensions.pygram_payment_source_dimension_factory,
     "etl_active": True},

    {"name": "payout_method",
     "source_sql": SOURCE_QUERIES["PAYOUT_METHOD"],
     "create_sql": CREATE_QUERIES["PAYOUT_METHOD"],
     "dimension_handler": dimensions.pygram_payout_method_dimension_factory,
     "etl_active": True},

    {"name": "disability_program",
     "source_sql": SOURCE_QUERIES["DISABILITY_PROGRAM"],
     "create_sql": CREATE_QUERIES["DISABILITY_PROGRAM"],
     "dimension_handler": dimensions.pygram_disability_program_dimension,
     "etl_active": True},

    {"name": "affiliate",
     "source_sql": SOURCE_QUERIES["AFFILIATE"],
     "create_sql": CREATE_QUERIES["AFFILIATE"],
     "dimension_handler": dimensions.pygram_affiliate_dimension_factory,
     "etl_active": True},

    {"name": "site",
     "source_sql": SOURCE_QUERIES["SITE"],
     "create_sql": CREATE_QUERIES["SITE"],
     "dimension_handler": dimensions.pygram_site_dimension_factory,
     "etl_active": True},

    {"name": "credit_campaign",
     "source_sql": SOURCE_QUERIES["CREDIT_CAMPAIGN"],
     "create_sql": CREATE_QUERIES["CREDIT_CAMPAIGN"],
     "dimension_handler": dimensions.pygram_credit_campaign_factory,
     "etl_active": True}
]


fact_configs = [
    {"name": "product_sale",
     "source_sql": SOURCE_QUERIES["PRODUCT_SALE_FACT"],
     "create_sql": CREATE_QUERIES["PRODUCT_SALE_FACT"],
     "fact_handler": facts.pygram_product_sale_fact_factory,
     "etl_active": True},

    {"name": "product_upload",
     "source_sql": SOURCE_QUERIES["PRODUCT_UPLOAD_FACT"],
     "create_sql": CREATE_QUERIES["PRODUCT_UPLOAD_FACT"],
     "fact_handler": facts.pygram_product_upload_fact_factory,
     "etl_active": True},

    {"name": "account_registration",
     "source_sql": SOURCE_QUERIES["ACCOUNT_REGISTRATION_FACT"],
     "init_sql": CREATE_QUERIES["ACCOUNT_REGISTRATION_FACT"],
     "fact_handler": facts.pygram_account_registration_fact_factory,
     "etl_active": False},

    {"name": "credit_redemption",
     "source_sql": SOURCE_QUERIES["CREDIT_REDEMPTION_FACT"],
     "init_sql": CREATE_QUERIES["CREDIT_REDEMPTION_FACT"],
     "fact_handler": facts.pygram_credit_redemption_fact_factory,
     "etl_active": False},

    {"name": "disability_enrollment",
     "source_sql": SOURCE_QUERIES["DISABILITY_ENROLLMENT_FACT"],
     "init_sql": CREATE_QUERIES["DISABILITY_ENROLLMENT_FACT"],
     "fact_handler": facts.pygram_disability_enrollment_fact_factory,
     "etl_active": False},

    {"name": "payout",
     "source_sql": SOURCE_QUERIES["PAYOUT_FACT"],
     "init_sql": CREATE_QUERIES["PAYOUT_FACT"],
     "fact_handler": facts.pygram_payout_fact_factory,
     "etl_active": False},

    {"name": "product_review",
     "source_sql": SOURCE_QUERIES["PRODUCT_REVIEW_FACT"],
     "init_sql": CREATE_QUERIES["PRODUCT_REVIEW_FACT"],
     "fact_handler": facts.pygram_product_review_fact_factory,
     "etl_active": False},

]
