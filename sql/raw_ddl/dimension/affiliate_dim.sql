CREATE TABLE `affiliate_dim` (
  `id` int(11) NOT NULL,
  `affiliate_id` int(11) DEFAULT NULL,
  `name` varchar(75) DEFAULT NULL,
  `program_notetakers` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8