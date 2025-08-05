CREATE TABLE `fee_rate_report_action_error` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `fee_rate_error_report_uuid` char(26) NOT NULL,
  `action_error_uuid` char(26) NOT NULL,
  `action_type` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_rate_report_action_error_key1` (`uuid`),
  UNIQUE KEY `fee_rate_report_action_error_key2` (`fee_rate_error_report_uuid`,`id`)
);