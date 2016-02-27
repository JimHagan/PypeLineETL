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
) ENGINE=InnoDB DEFAULT CHARSET=utf8