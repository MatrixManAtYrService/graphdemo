CREATE TABLE `fee_rate_error_report` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `currency` char(3) NOT NULL,
  `apply_type` enum('DEFAULT','PER_ITEM','PERCENTAGE','BOTH','NONE','FLAT') DEFAULT NULL,
  `resolved_status` smallint DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_rate_error_report_key1` (`uuid`)
);