CREATE TABLE `site_dim` (
  `id` int(11) NOT NULL,
  `site_id` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `domain` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8