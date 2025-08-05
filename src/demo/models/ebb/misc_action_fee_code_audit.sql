CREATE TABLE `misc_action_fee_code_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `misc_action_fee_code_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `misc_specifier` varchar(25) NOT NULL,
  `misc_action_type` varchar(25) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `fee_category` varchar(25) DEFAULT NULL,
  `fee_code` varchar(25) DEFAULT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  `modified_timestamp` datetime(6) DEFAULT NULL,
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `misc_action_fee_code_audit_key1` (`uuid`,`id`)
);