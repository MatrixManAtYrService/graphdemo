CREATE TABLE `monetary_adjustment` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `adjust_fee_summary_uuid` char(26) NOT NULL,
  `qualified_fee_summary_uuid` char(26) NOT NULL,
  `rule_uuid` char(26) NOT NULL,
  `rule_criteria_uuid` varchar(26) DEFAULT NULL,
  `rule_type` enum('AUTO_ADJUST','TIERED') NOT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_adjustment_key1` (`uuid`),
  UNIQUE KEY `monetary_adjustment_key2` (`billing_entity_uuid`,`adjust_fee_summary_uuid`,`qualified_fee_summary_uuid`,`rule_uuid`,`rule_criteria_uuid`,`id`),
  UNIQUE KEY `monetary_adjustment_key3` (`adjust_fee_summary_uuid`,`qualified_fee_summary_uuid`,`rule_uuid`,`rule_criteria_uuid`,`id`),
  UNIQUE KEY `monetary_adjustment_key4` (`qualified_fee_summary_uuid`,`adjust_fee_summary_uuid`,`rule_uuid`,`rule_criteria_uuid`,`id`),
  UNIQUE KEY `monetary_adjustment_key5` (`rule_uuid`,`rule_criteria_uuid`,`rule_type`,`billing_entity_uuid`,`adjust_fee_summary_uuid`,`id`)
);