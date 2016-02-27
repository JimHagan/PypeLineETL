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