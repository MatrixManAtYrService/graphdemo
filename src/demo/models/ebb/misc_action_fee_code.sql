CREATE TABLE `misc_action_fee_code` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `misc_specifier` varchar(25) NOT NULL,
  `misc_action_type` varchar(25) NOT NULL,
  `effective_date` date NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `misc_action_fee_code_key1` (`uuid`),
  UNIQUE KEY `misc_action_fee_code_key2` (`misc_specifier`,`misc_action_type`,`effective_date`)
);