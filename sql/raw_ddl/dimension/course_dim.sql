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
) ENGINE=InnoDB DEFAULT CHARSET=utf8