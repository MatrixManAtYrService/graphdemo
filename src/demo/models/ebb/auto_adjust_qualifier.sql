CREATE TABLE `auto_adjust_qualifier` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `auto_adjust_rule_uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `negate_fee_summary` smallint NOT NULL DEFAULT '0',
  `disqualify` smallint NOT NULL DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_adjust_qualifier_key1` (`uuid`),
  UNIQUE KEY `auto_adjust_qualifier_key2` (`auto_adjust_rule_uuid`,`fee_category`,`fee_code`)
);