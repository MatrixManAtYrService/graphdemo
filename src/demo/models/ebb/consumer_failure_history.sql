CREATE TABLE `consumer_failure_history` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `environment` char(25) NOT NULL,
  `reference_id` char(13) NOT NULL,
  `payload` text NOT NULL,
  `channel` varchar(127) DEFAULT NULL,
  `topic` varchar(127) DEFAULT NULL,
  `cause` varchar(100) NOT NULL,
  `message` varchar(500) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `consumer_failure_history_index1` (`reference_id`,`created_timestamp`)
);