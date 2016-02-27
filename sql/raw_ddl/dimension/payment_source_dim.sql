CREATE TABLE `payment_source_dim` (
  `id` int(11) NOT NULL,
  `payment_sourcetype_id` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
