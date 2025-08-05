CREATE TABLE `monetary_rule_set_rule_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `monetary_rule_set_rule_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `monetary_rule_set_uuid` char(26) DEFAULT NULL,
  `rule_uuid` char(26) DEFAULT NULL,
  `rule_type` enum('AUTO_ADJUST','TIERED') DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_rule_set_rule_audit_key1` (`uuid`,`id`)
);