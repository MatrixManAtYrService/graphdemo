CREATE TABLE `monetary_rule_set_rule` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `monetary_rule_set_uuid` char(26) NOT NULL,
  `rule_uuid` char(26) NOT NULL,
  `rule_type` enum('AUTO_ADJUST','TIERED') NOT NULL,
  `effective_date` date NOT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_rule_set_rule_key1` (`uuid`),
  UNIQUE KEY `monetary_rule_set_rule_key2` (`rule_uuid`,`effective_date`,`id`),
  UNIQUE KEY `monetary_rule_set_rule_key3` (`effective_date`,`rule_uuid`,`id`),
  UNIQUE KEY `monetary_rule_set_rule_key4` (`monetary_rule_set_uuid`,`effective_date`,`rule_uuid`,`id`)
);