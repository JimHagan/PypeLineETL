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