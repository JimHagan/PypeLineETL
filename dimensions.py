from pygrametl.tables import Dimension

"""
This module contains factory parameters for various pygrametl Dimension
instances.  These will be used to do the heavy lifting
within the ETL pipeline.
"""

pygram_product_dimension_factory = {
    "class": Dimension,
    "name": 'product_dim',
    "key": 'id',
    "attributes": ['product_id', 'name', 'product_class', 'item_id',
                    'created_date', 'creator_username', 'school_name', 'school_short_name',
                    'school_state', 'a_head_id', 'a_head_code', 'a_head_name',
                    'school_subject_id', 'school_subject_code',
                    'school_subject_name', 'course_id', 'course_code',
                    'course_name', 'affiliate_name', 'brand_name',
                    'profanity_score', 'flagged_phrase_score', 'plagiarism_score',
                    'deactivation_reason', 'pagecount'],
    "lookupatts": ['product_id']
}

pygram_user_dimension_factory = {
    "class": Dimension,
    "name": 'user_dim',
    "key": 'id',
    "attributes": ['user_id', 'username', 'first_name', 'last_name', 'email',
                'join_datetime', 'registration_source', 'channel_source',
                'enrollment_level', 'gpa', 'graduation_year', 'major',
                'payout_method', 'timezone', 'school_name',
                'school_short_name', 'school_state', 'tutor', 'social_user',
                'staff_user', 'disability_seller', 'disability_client',
                'disability_director', 'affiliate', 'buyer', 'uploader',
                'seller', 'first_purchase_date', 'first_upload_date',
                'first_sale_date', 'last_purchase_date', 'last_upload_date',
                'last_sale_date'],
    "lookupatts": ['user_id']
}

pygram_course_dimension_factory = {
    "class": Dimension,
    "name": 'course_dim',
    "key": 'id',
    "attributes": ['course_id', 'code', 'name', 'school_name',
                'school_short_name', 'school_state',
                'a_head_id', 'a_head_code', 'a_head_name',
                'school_subject_id', 'school_subject_code',
                'school_subject_name'],
    "lookupatts": ['course_id']
}

pygram_date_dimension_factory = {
    "class": Dimension,
    "name": 'date_dim',
    "key": 'date_key',
    "attributes": ['full_date','day_of_week','day_num_in_month',
                   'day_num_overall','day_name','day_abbrev','weekday_flag',
                   'week_num_in_year','week_num_overall','week_begin_date',
                   'week_begin_date_key','month','month_num_overall',
                   'month_name','month_abbrev','quarter','year','yearmo',
                   'fiscal_month','fiscal_quarter','fiscal_year',
                   'last_day_in_month_flag','same_day_year_ago'],
    "lookupatts": []
}

pygram_school_dimension_factory = {
    "class": Dimension,
    "name": 'school_dim',
    "key": 'id',
    "attributes": ['school_id', 'name', 'short_name', 'city',
                'state', 'city_state', 'zipcode', 'enrollment', 'term_type',
                'curated_subjects'],
    "lookupatts": ['school_id']
}

pygram_payment_source_dimension_factory = {
    "class": Dimension,
    "name": 'payment_source_dim',
    "key": 'id',
    "attributes": ['payment_sourcetype_id', 'name', 'code'],
    "lookupatts": ['payment_sourcetype_id']
}

pygram_payout_method_dimension_factory = {
    "class": Dimension,
    "name": 'payout_method_dim',
    "key": 'id',
    "attributes": ['payoutchoice_id', 'name'],
    "lookupatts": ['payoutchoice_id']
}

pygram_disability_program_dimension = {
    "class": Dimension,
    "name": 'disability_program_dim',
    "key": 'id',
    "attributes": ['disability_program_id', 'school_name', 'school_short_name',
                   'program_notetakers', 'program_clients', 'program_directors'],
    "lookupatts": ['disability_program_id']}

pygram_affiliate_dimension_factory = {
    "class": Dimension,
    "name": 'affiliate_dim',
    "key": 'id',
    "attributes": ['affiliate_id', 'name', 'program_notetakers'],
    "lookupatts": ['affiliate_id']
}

pygram_site_dimension_factory = {
    "class": Dimension,
    "name": 'site_dim',
    "key": 'id',
    "attributes": ["site_id", "domain", "name"],
    "lookupatts": ['site_id']
}

pygram_credit_campaign_factory = {
    "class": Dimension,
    "name": 'credit_campaign_dim',
    "key": 'id',
    "attributes": ['credit_campaign_id', 'name', 'created_date',
                   'channel_partner', 'code_count', 'code_denomination',
                   'repeat_use', 'start_date', 'end_date', 'valid_date',
                   'expiration_date', 'funding_account_type',
                   'funding_account_id', 'funding_account_name'],
    "lookupatts": ['credit_campaign_id']
}
