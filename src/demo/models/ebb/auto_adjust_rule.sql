CREATE TABLE `auto_adjust_rule` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `rule_status` enum('SETUP','ACTIVE','DEPRECATED','DELETED') NOT NULL DEFAULT 'SETUP',
  `rule_alias` varchar(25) DEFAULT NULL,
  `rate_fee_category` varchar(25) NOT NULL,
  `rate_fee_code` varchar(25) NOT NULL,
  `target_entity_type` enum('MERCHANT','RESELLER','DEVELOPER') NOT NULL,
  `short_desc` varchar(40) NOT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_adjust_rule_key1` (`uuid`),
  UNIQUE KEY `auto_adjust_rule_key2` (`rule_status`,`target_entity_type`,`rate_fee_category`,`rate_fee_code`,`id`),
  UNIQUE KEY `auto_adjust_rule_key3` (`rule_alias`,`uuid`)
);