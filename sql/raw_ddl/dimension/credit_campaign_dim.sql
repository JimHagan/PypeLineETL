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
) ENGINE=InnoDB DEFAULT CHARSET=utf8