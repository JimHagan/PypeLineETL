QUERIES = {
    "PRODUCT":
    '''
    SELECT p.id as product_id,
           p.title as name,
           pcl.name as product_class,
           p.object_id as item_id,
           p.date_created as created_date,
           u.username as creator_username,
           sch.name as school_name,
           sch.short_name as school_short_name,
           sch.state as school_state,
           1 as a_head_id,
           'ahd123' as a_head_code,
           'A-Head subject 123' as a_head_name,
           p.subject_id as school_subject_id,
           schsubj.code as school_subject_code,
           schsubj.name as school_subject_name,
           p.course_id as course_id,
           cour.code as course_code,
           cour.name as course_name,
           aff.name as affiliate_name,
           brand.name as brand_name,
           audit.profanity_score as profanity_score,
           audit.keyword_score as flagged_phrase_score,
           audit.plagiarism_score as plagiarism_score,
           '' as deactivation_reason,
           0 as pagecount
    FROM catalogue_product p
    LEFT JOIN catalogue_productclass pcl ON p.product_class_id=pcl.id
    LEFT JOIN auth_user u ON p.creator_id=u.id
    LEFT JOIN schools_school sch ON p.school_id=sch.id
    LEFT JOIN courses_course cour ON p.course_id=cour.id
    LEFT JOIN affiliate_affiliate aff ON p.affiliate_brand_id=aff.id
    LEFT JOIN brand_brand brand ON p.brand_id=brand.id
    LEFT JOIN contentquality_contentaudit audit ON audit.product_id=p.id
    LEFT JOIN courses_subject schsubj ON p.subject_id=schsubj.id
    ;
    ''',

    "USER":
    '''
     SELECT u.id as user_id,
            u.username as username,
            IF(LENGTH(u.first_name) > 0, u.first_name, 'Unknown') as first_name,
            IF(LENGTH(u.last_name) > 0, u.last_name, 'Unknown') as last_name,
            u.email as email,
            u.date_joined as join_datetime,
            IF(LENGTH(prof.registration_source) > 0, prof.registration_source, 'Unknown') as registration_source,
            IF(LENGTH(prof.channel_source) > 0, prof.channel_source, 'Unknown') as channel_source,
            CASE prof.enrollment_level
                WHEN 1 THEN 'Undergrad'
                WHEN 2 THEN 'Graduate'
                ELSE 'Unknown'
            END as enrollment_level,
            CASE prof.gpa
                WHEN -1 THEN 'Do not display'
                WHEN 0 THEN 'Under 2.0'
                WHEN 1 THEN '2.0-2.5'
                WHEN 2 THEN '2.5-3.0'
                WHEN 3 THEN '3.0-3.5'
                WHEN 4 THEN '3.5-4.0'
            END as gpa,
            IF(prof.gradyear IS NULL, 0000, prof.gradyear) as graduation_year,
            IF(LENGTH(prof.major) > 0, prof.major, 'Unknown') as major,
            IF(pyc.name IS NULL, 'Unknown', pyc.name) as payout_method,
            CASE prof.preferred_timezone
                WHEN 0 THEN 'US/Hawaii'
                WHEN 1 THEN 'US/Alaska'
                WHEN 2 THEN 'US/Pacific'
                WHEN 3 THEN 'US/Arizona'
                WHEN 4 THEN 'US/Mountain'
                WHEN 5 THEN 'US/Central'
                WHEN 6 THEN 'US/Eastern'
                WHEN 7 THEN 'Canada/Atlantic'
            END as timezone,
            IF(LENGTH(sch.name) > 0, sch.name, 'Unknown') as school_name,
            IF(LENGTH(sch.short_name) > 0, sch.short_name, 'Unknown') as school_short_name,
            IF(LENGTH(sch.state) > 0, sch.state, 'XX') as school_state,
            IF(tp.id IS NULL, 'Non-Tutor', 'Tutor') as tutor,
            IF(dsr1.id IS NULL, 'Non-Disability Seller', 'Disability Seller') as disability_seller,
            IF(dsr2.id IS NULL, 'Non-Disability Client', 'Disability Client') as disability_client,
            IF(dsr3.id IS NULL, 'Non-Disability Director', 'Disability Director') as disability_director,
            IF(affu.id IS NULL, 'Non-Affiliated', aff.name) as affiliate,
            IF(usa.id IS NULL, 'Non-Social', 'Social') as social_user,
            IF(u.is_staff, 'Staff User', 'Non-Staff User') as staff_user,
            IF(MAX(o.total_excl_tax) > 0, 'Buyer', 'Non-Buyer') as buyer,
            IF(COUNT(cp.id) > 0, 'Uploader', 'Non-Uploader') as uploader,
            if(MAX(ol.line_price_excl_tax) > 0, 'Seller', 'Non-Seller') as seller,
            MIN(DATE(o.date_placed)) as first_purchase_date,
            MIN(DATE(cp.date_created)) as first_upload_date,
            MIN(DATE(o2.date_placed)) as first_sale_date,
            MAX(DATE(o.date_placed)) as last_purchase_date,
            MAX(DATE(cp.date_created)) as last_upload_date,
            MAX(DATE(o2.date_placed)) as last_sale_date
     FROM auth_user u
     LEFT JOIN profiles_profile prof ON u.id=prof.user_id
     LEFT JOIN schools_school sch ON prof.school_id=sch.id
     LEFT JOIN profiles_payoutchoice pyc ON prof.payout_method_id=pyc.id
     LEFT JOIN tutor_tutoringprofile tp ON tp.user_id=u.id
     LEFT JOIN disability_dsuserrole dsr1 ON dsr1.user_id = u.id AND dsr1.role='notetaker'
     LEFT JOIN disability_dsuserrole dsr2 ON dsr2.user_id = u.id AND dsr2.role='client'
     LEFT JOIN disability_dsuserrole dsr3 ON dsr3.user_id = u.id AND dsr3.role='director'
     LEFT JOIN affiliate_affiliateuser affu ON affu.user_id = u.id
     LEFT JOIN affiliate_affiliate aff ON affu.affiliate_id = aff.id
     LEFT JOIN social_auth_usersocialauth usa ON usa.user_id = u.id
     LEFT JOIN order_order o ON o.user_id = u.id
     LEFT JOIN catalogue_product cp ON cp.creator_id = u.id
     LEFT JOIN order_line ol on ol.product_id = cp.id
     LEFT JOIN order_order o2 ON ol.order_id = o2.id
     GROUP BY u.id
     ;
    ''',

    "COURSE":
    '''
    SELECT c.id as course_id,
           c.code as code,
           c.name as name,
           sch.name as school_name,
           sch.short_name as school_short_name,
           sch.state as school_state,
           1 as a_head_id,
           'ahd123' as a_head_code,
           'A-Head subject 123' as a_head_name,
           schsubj.id as school_subject_id,
           schsubj.code as school_subject_code,
           schsubj.name as school_subject_name
    FROM courses_course c
    LEFT JOIN schools_school sch ON c.school_id=sch.id
    LEFT JOIN courses_subject schsubj ON c.subject_id=schsubj.id
    ;
    ''',

    "DATE": 'CSV',

    "SCHOOL":
    '''
    SELECT sch.id as school_id,
           sch.name as name,
           sch.short_name as short_name,
           sch.city as city,
           sch.state as state,
           IF(sch.city = '', sch.state, CONCAT(sch.city, ', ', sch.state)) as city_state,
           sch.zipcode as zipcode,
           sch.enrollment as enrollment,
           CASE sch.term_type
              WHEN 1 THEN 'Annual'
              WHEN 2 THEN 'Semester'
              WHEN 3 THEN 'Trimester'
              WHEN 4 THEN 'Quarter'
           END as term_type,
           IF(sch.has_curated_subjects = 0, "No Curated Subjects", "Has Curated Subjects") as curated_subjects
    FROM schools_school sch;
    ''',

    "PAYMENT_SOURCE":
    '''
    SELECT pst.id as payment_sourcetype_id,
           pst.name as name,
           pst.code as code
    FROM payment_sourcetype pst;
    ''',

    "PAYOUT_METHOD":
    '''
    SELECT pyc.id as payoutchoice_id,
           pyc.name as name
    FROM profiles_payoutchoice pyc
    ''',

    "DISABILITY_PROGRAM":
    '''
    SELECT dp.id as disability_program_id,
           IF(LENGTH(sch.name) > 0, sch.name, 'Unknown') as school_name,
           IF(LENGTH(sch.short_name) > 0, sch.short_name, 'Unknown') as school_short_name,
		   IF(COUNT(dsr1.id) > 0, 'Has Notetakers', 'No Notetakers') as program_notetakers,
		   IF(COUNT(dsr2.id) > 0, 'Has Clients', 'No Clients') as program_clients,
		   IF(COUNT(dsr3.id) > 0, 'Has Directors', 'No Directors') as program_directors
    FROM disability_program dp
    LEFT JOIN schools_school sch ON dp.school_id=sch.id
    LEFT JOIN disability_dsuserrole dsr1 ON dsr1.program_id = dp.id AND dsr1.role = 'notetaker'
    LEFT JOIN disability_dsuserrole dsr2 ON dsr2.program_id = dp.id AND dsr2.role = 'client'
    LEFT JOIN disability_dsuserrole dsr3 ON dsr3.program_id = dp.id AND dsr3.role = 'director'
    GROUP BY dp.id
    ;
    ''',

    "AFFILIATE":
    '''
    SELECT aff.id as affiliate_id,
           aff.name as name,
		   IF(COUNT(afu.id) > 0, 'Has Notetakers', 'No Notetakers') as program_notetakers
    FROM affiliate_affiliate aff
    LEFT JOIN affiliate_affiliateuser afu on afu.affiliate_id = aff.id
    GROUP By aff.id
    ''',

    "SITE":
    '''
    SELECT s.id as site_id, s.name as name, s.domain as domain
    FROM django_site s;
    ''',

    "CREDIT_CAMPAIGN":
    '''
    SELECT cc.id as credit_campaign_id,
           cc.name as name,
           DATE(cc.date_created) as created_date,
           ccp.name as channel_partner,
           COUNT(ccc.id) as code_count,
           cc.denomination as code_denomination,
           cc.repeat_use as repeat_use,
           DATE(cc.start_date) as start_date,
           DATE(cc.end_date) as end_date,
           DATE(cc.valid_date) as valid_date,
           DATE(cc.expiration_date) as expiration_date,
           act.name as funding_account_type,
           acc.id as funding_account_id,
           acc.name as funding_account_name
    FROM credit_creditcampaign cc
    LEFT JOIN campaign_channelpartner ccp ON cc.channel_partner_id = ccp.id
	LEFT JOIN credit_creditcampaigncode ccc on ccc.campaign_id = cc.id
	LEFT JOIN accounts_account acc on cc.funding_account_id = acc.id
	LEFT JOIN accounts_accounttype act on acc.account_type_id = act.id
	GROUP BY cc.id
    ''',

    "ACCOUNT_REGISTRATION_FACT": '',

    "CREDIT_REDEMPTION_FACT": '',

    "DISABILITY_ENROLLMENT_FACT": '',

    "PAYOUT_FACT": '',

    "PRODUCT_REVIEW_FACT": '',

    "PRODUCT_SALE_FACT":
    '''
    SELECT ol.quantity as quantity,
           ol.line_price_excl_tax as extended_sales_amount,
           ol.line_price_before_discounts_excl_tax - ol.line_price_excl_tax as extended_discount_amount,
           1 as transaction_fee,
           ol.unit_retail_price as seller_unit_price,
           oo.date_placed as sale_datetime,
           cp.school_id as school_id,
           cp.course_id as course_id,
           cp.creator_id as seller_id,
           oo.user_id as buyer_id,
           cp.id as product_id,
           NULL as payment_source_fk,
           dp.id as seller_disability_program_id,
           NULL as buyer_disability_program_fk,
           NULL as bundle_purchased_fk,
           NULL as site_fk,
           NULL as affiliate_fk
    FROM order_line ol
    LEFT JOIN order_order oo ON ol.order_id = oo.id
    LEFT JOIN catalogue_product cp ON ol.product_id = cp.id
	LEFT JOIN disability_program_products dpp ON dpp.product_id = cp.id
	LEFT JOIN disability_program dp ON dpp.program_id = dp.id
    ''',

    "PRODUCT_UPLOAD_FACT":
    '''
    SELECT cp.id as product_id,
           cp.school_id as school_id,
           cp.course_id as course_id,
           cp.creator_id as seller_id,
           cp.date_created as upload_datetime,
           dp.id as seller_disability_program_id,
           NULL as site_fk,
           NULL as affiliate_fk
    FROM catalogue_product cp
	LEFT JOIN disability_program_products dpp ON dpp.product_id = cp.id
	LEFT JOIN disability_program dp ON dpp.program_id = dp.id
    ''',

}
