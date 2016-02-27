CREATE TABLE `disability_program_dim` (
  `id` int(11) NOT NULL,
  `disability_program_id` int(11) DEFAULT NULL,
  `school_name` varchar(75) DEFAULT NULL,
  `school_short_name` varchar(10) DEFAULT NULL,
  `program_notetakers` varchar(45) DEFAULT NULL,
  `program_clients` varchar(45) DEFAULT NULL,
  `program_directors` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8