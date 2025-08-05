CREATE TABLE `monetary_adjustment_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `monetary_adjustment_id` bigint unsigned NOT NULL,
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
  UNIQUE KEY `monetary_adjustment_mutation_key1` (`uuid`,`id`)
);