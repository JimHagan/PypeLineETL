QUERIES = {
    "PRODUCT":
    '''
    CREATE TABLE `product_dim` (
      `id` int(11) NOT NULL,
      `product_id` int(11) DEFAULT NULL,
      `name` varchar(75) DEFAULT NULL,
      `product_class` varchar(45) DEFAULT NULL,
      `item_id` int(11) DEFAULT NULL,
      `created_date` datetime DEFAULT NULL,
      `creator_username` varchar(30) DEFAULT NULL,
      `school_name` varchar(75) DEFAULT NULL,
      `school_short_name` varchar(10) DEFAULT NULL,
      `school_state` varchar(10) DEFAULT NULL,
      `a_head_id` int(11) DEFAULT NULL,
      `a_head_code` varchar(20) DEFAULT NULL,
      `a_head_name` varchar(100) DEFAULT NULL,
      `school_subject_id` int(11) DEFAULT NULL,
      `school_subject_code` varchar(10) DEFAULT NULL,
      `school_subject_name` varchar(75) DEFAULT NULL,
      `course_id` int(11) DEFAULT NULL,
      `course_code` varchar(20) DEFAULT NULL,
      `course_name` varchar(75) DEFAULT NULL,
      `affiliate_name` varchar(75) DEFAULT NULL,
      `brand_name` varchar(200) DEFAULT NULL,
      `profanity_score` int(11) DEFAULT NULL,
      `flagged_phrase_score` int(11) DEFAULT NULL,
      `plagiarism_score` int(11) DEFAULT NULL,
      `deactivation_reason` varchar(1024) DEFAULT NULL,
      `pagecount` int(11) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "USER":
    '''
    CREATE TABLE `user_dim` (
      `id` int(11) NOT NULL,
      `user_id` int(11) DEFAULT NULL,
      `username` varchar(30) DEFAULT NULL,
      `first_name` varchar(30) DEFAULT NULL,
      `last_name` varchar(30) DEFAULT NULL,
      `email` varchar(75) DEFAULT NULL,
      `join_datetime` datetime DEFAULT NULL,
      `registration_source` varchar(100) DEFAULT NULL,
      `social_user` varchar(45) DEFAULT NULL,
      `staff_user` varchar(45) DEFAULT NULL,
      `channel_source` varchar(200) DEFAULT NULL,
      `enrollment_level` varchar(45) DEFAULT NULL,
      `gpa` varchar(45) DEFAULT NULL,
      `graduation_year` int(11) DEFAULT NULL,
      `major` varchar(100) DEFAULT NULL,
      `payout_method` varchar(45) DEFAULT NULL,
      `timezone` varchar(45) DEFAULT NULL,
      `school_name` varchar(75) DEFAULT NULL,
      `school_short_name` varchar(10) DEFAULT NULL,
      `school_state` varchar(10) DEFAULT NULL,
      `tutor` varchar(45) DEFAULT NULL,
      `disability_seller` varchar(45) DEFAULT NULL,
      `disability_client` varchar(45) DEFAULT NULL,
      `disability_director` varchar(45) DEFAULT NULL,
      `affiliate` varchar(45) DEFAULT NULL,
      `buyer` varchar(45) DEFAULT NULL,
      `uploader` varchar(45) DEFAULT NULL,
      `seller` varchar(45) DEFAULT NULL,
      `first_purchase_date` date DEFAULT NULL,
      `first_upload_date` date DEFAULT NULL,
      `first_sale_date` date DEFAULT NULL,
      `last_purchase_date` date DEFAULT NULL,
      `last_upload_date` date DEFAULT NULL,
      `last_sale_date` date DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "COURSE":
    '''
    CREATE TABLE `course_dim` (
      `id` int(11) NOT NULL,
      `course_id` int(11) DEFAULT NULL,
      `name` varchar(75) DEFAULT NULL,
      `code` varchar(20) DEFAULT NULL,
      `school_name` varchar(75) DEFAULT NULL,
      `school_short_name` varchar(10) DEFAULT NULL,
      `school_state` varchar(10) DEFAULT NULL,
      `a_head_id` int(11) DEFAULT NULL,
      `a_head_code` varchar(20) DEFAULT NULL,
      `a_head_name` varchar(100) DEFAULT NULL,
      `school_subject_id` int(11) DEFAULT NULL,
      `school_subject_code` varchar(20) DEFAULT NULL,
      `school_subject_name` varchar(75) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;    ''',
    "DATE":
    '''
    CREATE TABLE `date_dim` (
      `date_key` int(8) NOT NULL,
      `full_date` date DEFAULT NULL,
      `day_of_week` tinyint(4) DEFAULT NULL,
      `day_num_in_month` tinyint(4) DEFAULT NULL,
      `day_num_overall` smallint(6) DEFAULT NULL,
      `day_name` varchar(9) DEFAULT NULL,
      `day_abbrev` char(3) DEFAULT NULL,
      `weekday_flag` varchar(7) DEFAULT NULL,
      `week_num_in_year` tinyint(4) DEFAULT NULL,
      `week_num_overall` smallint(6) DEFAULT NULL,
      `week_begin_date` date DEFAULT NULL,
      `week_begin_date_key` int(8) DEFAULT NULL,
      `month` tinyint(4) DEFAULT NULL,
      `month_num_overall` smallint(6) DEFAULT NULL,
      `month_name` varchar(9) DEFAULT NULL,
      `month_abbrev` char(3) DEFAULT NULL,
      `quarter` tinyint(4) DEFAULT NULL,
      `year` smallint(6) DEFAULT NULL,
      `yearmo` int(11) DEFAULT NULL,
      `fiscal_month` tinyint(4) DEFAULT NULL,
      `fiscal_quarter` tinyint(4) DEFAULT NULL,
      `fiscal_year` smallint(6) DEFAULT NULL,
      `last_day_in_month_flag` varchar(14) DEFAULT NULL,
      `same_day_year_ago` date DEFAULT NULL,
      PRIMARY KEY (`date_key`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "SCHOOL":
    '''
    CREATE TABLE `school_dim` (
      `id` int(11) NOT NULL,
      `school_id` int(11) DEFAULT NULL,
      `name` varchar(75) DEFAULT NULL,
      `short_name` varchar(10) DEFAULT NULL,
      `city` varchar(128) DEFAULT NULL,
      `state` varchar(10) DEFAULT NULL,
      `city_state` varchar(150) DEFAULT NULL,
      `zipcode` varchar(10) DEFAULT NULL,
      `enrollment` int(11) DEFAULT NULL,
      `term_type` varchar(45) DEFAULT NULL,
      `curated_subjects` varchar(30) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    ,
    "PAYMENT_SOURCE":
    '''
    CREATE TABLE `payment_source_dim` (
      `id` int(11) NOT NULL,
      `payment_sourcetype_id` int(11) DEFAULT NULL,
      `name` varchar(45) DEFAULT NULL,
      `code` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "PAYOUT_METHOD":
    '''
    CREATE TABLE `payout_method_dim` (
      `id` int(11) NOT NULL,
      `payoutchoice_id` int(11) DEFAULT NULL,
      `name` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "DISABILITY_PROGRAM":
    '''
    CREATE TABLE `disability_program_dim` (
      `id` int(11) NOT NULL,
      `disability_program_id` int(11) DEFAULT NULL,
      `school_name` varchar(75) DEFAULT NULL,
      `school_short_name` varchar(10) DEFAULT NULL,
      `program_notetakers` varchar(45) DEFAULT NULL,
      `program_clients` varchar(45) DEFAULT NULL,
      `program_directors` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "AFFILIATE":
    '''
    CREATE TABLE `affiliate_dim` (
      `id` int(11) NOT NULL,
      `affiliate_id` int(11) DEFAULT NULL,
      `name` varchar(75) DEFAULT NULL,
      `program_notetakers` varchar(45) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "SITE":
    '''
    CREATE TABLE `site_dim` (
      `id` int(11) NOT NULL,
      `site_id` int(11) DEFAULT NULL,
      `name` varchar(45) DEFAULT NULL,
      `domain` varchar(100) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "CREDIT_CAMPAIGN":
    '''
    CREATE TABLE `credit_campaign_dim` (
      `id` int(11) NOT NULL,
      `credit_campaign_id` int(11) DEFAULT NULL,
      `name` varchar(75) DEFAULT NULL,
      `created_date` date DEFAULT NULL,
      `channel_partner` varchar(75) DEFAULT NULL,
      `code_count` int(11) DEFAULT NULL,
      `code_denomination` decimal(10,2) DEFAULT NULL,
      `repeat_use` varchar(45) DEFAULT NULL,
      `start_date` date DEFAULT NULL,
      `end_date` date DEFAULT NULL,
      `valid_date` date DEFAULT NULL,
      `expiration_date` date DEFAULT NULL,
      `funding_account_type` varchar(45) DEFAULT NULL,
      `funding_account_id` int(11) DEFAULT NULL,
      `funding_account_name` varchar(128) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ''',
    "ACCOUNT_REGISTRATION_FACT":
    '''
    CREATE TABLE `account_registration_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `user_fk` int(11) DEFAULT NULL,
      `school_fk` int(11) DEFAULT NULL,
      `disability_program_fk` int(11) DEFAULT NULL,
      `affiliate_fk` int(11) DEFAULT NULL,
      `site_fk` int(11) DEFAULT NULL,
      `referral_utm_source` varchar(45) DEFAULT NULL,
      `referral_utm_medium` varchar(45) DEFAULT NULL,
      `referral_utm_campaign` varchar(45) DEFAULT NULL,
      `registration_datetime` datetime DEFAULT NULL,
      KEY `account_registration_date_idx` (`date_fk`),
      KEY `account_registration_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `account_registration_user_idx` (`user_fk`),
      KEY `account_registration_school_idx` (`school_fk`),
      KEY `account_registration_disability_program_idx` (`disability_program_fk`),
      KEY `account_registration_affiliate_idx` (`affiliate_fk`),
      KEY `account_registration_site_idx` (`site_fk`),
      CONSTRAINT `account_registration_affiliate` FOREIGN KEY (`affiliate_fk`) REFERENCES `affiliate_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_disability_program` FOREIGN KEY (`disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_school` FOREIGN KEY (`school_fk`) REFERENCES `school_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_site` FOREIGN KEY (`site_fk`) REFERENCES `site_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `account_registration_user` FOREIGN KEY (`user_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "CREDIT_REDEMPTION_FACT":
    '''
    CREATE TABLE `credit_redemption_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `buyer_fk` int(11) DEFAULT NULL,
      `site_fk` int(11) DEFAULT NULL,
      `credit_campaign_fk` int(11) DEFAULT NULL,
      `amount` decimal(10,2) DEFAULT NULL,
      `order_id` int(11) DEFAULT NULL,
      `order_total` decimal(10,2) DEFAULT NULL,
      `redemption_datetime` datetime DEFAULT NULL,
      KEY `credit_redemption_date_idx` (`date_fk`),
      KEY `credit_redemption_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `credit_redemption_buyer_idx` (`buyer_fk`),
      KEY `credit_redemption_site_idx` (`site_fk`),
      KEY `credit_redemption_credit_campaign_idx` (`credit_campaign_fk`),
      CONSTRAINT `credit_redemption_buyer` FOREIGN KEY (`buyer_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `credit_redemption_credit_campaign` FOREIGN KEY (`credit_campaign_fk`) REFERENCES `credit_campaign_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `credit_redemption_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `credit_redemption_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `credit_redemption_site` FOREIGN KEY (`site_fk`) REFERENCES `site_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "DISABILITY_ENROLLMENT_FACT":
    '''
    CREATE TABLE `disability_enrollment_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `disability_program_fk` int(11) DEFAULT NULL,
      `course_fk` int(11) DEFAULT NULL,
      `user_fk` int(11) DEFAULT NULL,
      `event_type` varchar(45) DEFAULT NULL,
      `event_datetime` datetime DEFAULT NULL,
      KEY `disability_enrollment_date_idx` (`date_fk`),
      KEY `disability_enrollment_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `disability_enrollment_disability_program_idx` (`disability_program_fk`),
      KEY `disability_enrollment_course_idx` (`course_fk`),
      KEY `disability_enrollment_user_idx` (`user_fk`),
      CONSTRAINT `disability_enrollment_course` FOREIGN KEY (`course_fk`) REFERENCES `course_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `disability_enrollment_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `disability_enrollment_disability_program` FOREIGN KEY (`disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `disability_enrollment_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `disability_enrollment_user` FOREIGN KEY (`user_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "PAYOUT_FACT":
    '''
    CREATE TABLE `payout_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `user_fk` int(11) DEFAULT NULL,
      `payout_method_fk` int(11) DEFAULT NULL,
      `disability_program_fk` int(11) DEFAULT NULL,
      `payout_amount` decimal(10,2) DEFAULT NULL,
      `sales_payout_amount` decimal(10,2) DEFAULT NULL,
      `non_sales_payout_amount` decimal(10,2) DEFAULT NULL,
      `payout_datetime` datetime DEFAULT NULL,
      KEY `payout_date_idx` (`date_fk`),
      KEY `payout_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `payout_user_idx` (`user_fk`),
      KEY `payout_payout_method_idx` (`payout_method_fk`),
      KEY `payout_disability_program_idx` (`disability_program_fk`),
      CONSTRAINT `payout_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `payout_disability_program` FOREIGN KEY (`disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `payout_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `payout_payout_method` FOREIGN KEY (`payout_method_fk`) REFERENCES `payout_method_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `payout_user` FOREIGN KEY (`user_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "PRODUCT_REVIEW_FACT":
    '''
    CREATE TABLE `product_review_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `product_fk` int(11) DEFAULT NULL,
      `seller_fk` int(11) DEFAULT NULL,
      `buyer_fk` int(11) DEFAULT NULL,
      `site_fk` int(11) DEFAULT NULL,
      `score` int(11) DEFAULT NULL,
      `comments` varchar(45) DEFAULT NULL,
      `review_datetime` datetime DEFAULT NULL,
      KEY `product_review_date_idx` (`date_fk`),
      KEY `product_review_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `product_review_product_idx` (`product_fk`),
      KEY `product_review_seller_idx` (`seller_fk`),
      KEY `product_review_buyer_idx` (`buyer_fk`),
      KEY `product_review_site_idx` (`site_fk`),
      CONSTRAINT `product_review_buyer` FOREIGN KEY (`buyer_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_review_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_review_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_review_product` FOREIGN KEY (`product_fk`) REFERENCES `product_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_review_seller` FOREIGN KEY (`seller_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_review_site` FOREIGN KEY (`site_fk`) REFERENCES `site_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "PRODUCT_SALE_FACT":
    '''
    CREATE TABLE `product_sale_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `product_fk` int(11) DEFAULT NULL,
      `school_fk` int(11) DEFAULT NULL,
      `course_fk` int(11) DEFAULT NULL,
      `seller_fk` int(11) DEFAULT NULL,
      `buyer_fk` int(11) DEFAULT NULL,
      `payment_source_fk` int(11) DEFAULT NULL,
      `seller_disability_program_fk` int(11) DEFAULT NULL,
      `buyer_disability_program_fk` int(11) DEFAULT NULL,
      `site_fk` int(11) DEFAULT NULL,
      `bundle_purchased_fk` int(11) DEFAULT NULL,
      `affiliate_fk` int(11) DEFAULT NULL,
      `extended_sales_amount` decimal(10,2) DEFAULT NULL,
      `quantity` int(11) DEFAULT NULL,
      `seller_unit_price` decimal(10,2) DEFAULT NULL,
      `transaction_fee` decimal(10,2) DEFAULT NULL,
      `extended_discount_amount` decimal(10,2) DEFAULT NULL,
      `sale_datetime` datetime DEFAULT NULL,
      KEY `product_sale_product_idx` (`product_fk`),
      KEY `product_sale_seller_idx` (`seller_fk`),
      KEY `product_sale_buyer_idx` (`buyer_fk`),
      KEY `product_sale_date_idx` (`date_fk`),
      KEY `product_sale_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `product_sale_school_idx` (`school_fk`),
      KEY `product_sale_payment_source_idx` (`payment_source_fk`),
      KEY `product_sale_seller_disability_program_idx` (`seller_disability_program_fk`),
      KEY `product_sale_buyer_disability_program_idx` (`buyer_disability_program_fk`),
      KEY `product_sale_site_idx` (`site_fk`),
      KEY `product_sale_bundle_purchased_idx` (`bundle_purchased_fk`),
      KEY `product_sale_course_idx` (`course_fk`),
      KEY `product_sale_affiliate_idx` (`affiliate_fk`),
      CONSTRAINT `product_sale_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_seller` FOREIGN KEY (`seller_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_buyer` FOREIGN KEY (`buyer_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_school` FOREIGN KEY (`school_fk`) REFERENCES `school_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_course` FOREIGN KEY (`course_fk`) REFERENCES `course_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_payment_source` FOREIGN KEY (`payment_source_fk`) REFERENCES `payment_source_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_seller_disability` FOREIGN KEY (`seller_disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_buyer_disability` FOREIGN KEY (`buyer_disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_site` FOREIGN KEY (`site_fk`) REFERENCES `site_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_bundle_purchased` FOREIGN KEY (`bundle_purchased_fk`) REFERENCES `product_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_affiliate` FOREIGN KEY (`affiliate_fk`) REFERENCES `affiliate_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_sale_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',
    "PRODUCT_UPLOAD_FACT":
    '''
    CREATE TABLE `product_upload_fact` (
      `date_fk` int(11) DEFAULT NULL,
      `flashnotes_date_fk` int(11) DEFAULT NULL,
      `product_fk` int(11) DEFAULT NULL,
      `school_fk` int(11) DEFAULT NULL,
      `course_fk` int(11) DEFAULT NULL,
      `seller_fk` int(11) DEFAULT NULL,
      `seller_disability_program_fk` int(11) DEFAULT NULL,
      `site_fk` int(11) DEFAULT NULL,
      `upload_datetime` datetime DEFAULT NULL,
      `affiliate_fk` int(11) DEFAULT NULL,
      KEY `product_upload_product_fk_idx` (`product_fk`),
      KEY `product_upload_school_fk_idx` (`school_fk`),
      KEY `product_upload_date_idx` (`date_fk`),
      KEY `product_upload_flashnotes_date_idx` (`flashnotes_date_fk`),
      KEY `product_upload_course_idx` (`course_fk`),
      KEY `product_upload_seller_idx` (`seller_fk`),
      KEY `product_upload_seller_disability_program_idx` (`seller_disability_program_fk`),
      KEY `product_upload_site_idx` (`site_fk`),
      KEY `product_upload_affiliate_idx` (`affiliate_fk`),
      CONSTRAINT `product_upload_affiliate` FOREIGN KEY (`affiliate_fk`) REFERENCES `affiliate_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_course` FOREIGN KEY (`course_fk`) REFERENCES `course_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_date` FOREIGN KEY (`date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_flashnotes_date` FOREIGN KEY (`flashnotes_date_fk`) REFERENCES `date_dim` (`date_key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_product` FOREIGN KEY (`product_fk`) REFERENCES `product_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_school` FOREIGN KEY (`school_fk`) REFERENCES `school_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_seller` FOREIGN KEY (`seller_fk`) REFERENCES `user_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_seller_disability_program` FOREIGN KEY (`seller_disability_program_fk`) REFERENCES `disability_program_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
      CONSTRAINT `product_upload_site` FOREIGN KEY (`site_fk`) REFERENCES `site_dim` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''',

}
