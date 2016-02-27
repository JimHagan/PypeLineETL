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
) ENGINE=InnoDB DEFAULT CHARSET=utf8