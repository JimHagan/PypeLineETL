from pygrametl.tables import FactTable

"""
This module contains factory parameters for various pygrametl FactTable
instances.  These will be used to do the heavy lifting
within the ETL pipeline.
"""

pygram_product_sale_fact_factory = {
    "class": FactTable,
    "name": 'product_sale_fact',
    "measures": ['extended_sales_amount',
                 'transaction_fee',
                 'extended_discount_amount',
                 'seller_unit_price',
                 'quantity',
                 'sale_datetime'],
    "timestamp_field": 'sale_datetime',
    "keyrefs": ['date_fk',
                'flashnotes_date_fk',
                'product_fk',
                'school_fk',
                'course_fk',
                'seller_fk',
                'buyer_fk',
                'payment_source_fk',
                'seller_disability_program_fk',
                'buyer_disability_program_fk',
                'site_fk',
                'bundle_purchased_fk',
                'affiliate_fk'],
}


pygram_product_upload_fact_factory = {
    "class": FactTable,
    "name": 'product_upload_fact',
    "measures": ['upload_datetime'],
    "timestamp_field": 'upload_datetime',
    "keyrefs": ['date_fk',
                'flashnotes_date_fk',
                'product_fk',
                'school_fk',
                'course_fk',
                'seller_fk',
                'seller_disability_program_fk',
                'site_fk',
                'affiliate_fk'],
}


pygram_account_registration_fact_factory = {
    "class": FactTable,
    "name": 'account_registration_fact',
    "measures": [],
    "keyrefs": ['date_fk',
                'user_fk',
                'school_fk',
                'disability_program_fk',
                'site_fk',
                'affiliate_fk'],
}


pygram_credit_redemption_fact_factory = {
    "class": FactTable,
    "name": 'credit_redemption_fact',
    "measures": ['amount'],
    "keyrefs": ['date_fk',
                'buyer_fk',
                'site_fk',
                'credit_campaign_fk'],
}


pygram_disability_enrollment_fact_factory = {
    "class": FactTable,
    "name": 'disability_enrollment_fact',
    "measures": [],
    "keyrefs": ['date_fk',
                'user_fk',
                'course_fk',
                'disability_program_fk'],
}


pygram_payout_fact_factory = {
    "class": FactTable,
    "name": 'payout_fact',
    "measures": ['payout_amount',
                 'sales_payout_amount',
                 'non_sales_payout_amount'],
    "keyrefs": ['date_fk',
                'user_fk',
                'disability_program_fk',
                'payout_method_fk'],
}


pygram_product_review_fact_factory = {
    "class": FactTable,
    "name": 'product_review_fact',
    "measures": [],
    "keyrefs": ['date_fk',
                'product_fk',
                'seller_fk',
                'buyer_fk',
                'site_fk',
                'bundle_purchased_fk'],
}
