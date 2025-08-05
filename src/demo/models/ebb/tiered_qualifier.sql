CREATE TABLE `tiered_qualifier` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `tiered_rule_uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `negate_fee_summary` smallint NOT NULL DEFAULT '0',
  `disqualify` smallint NOT NULL DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tiered_qualifier_key1` (`uuid`),
  UNIQUE KEY `tiered_qualifier_key2` (`tiered_rule_uuid`,`fee_category`,`fee_code`)
);