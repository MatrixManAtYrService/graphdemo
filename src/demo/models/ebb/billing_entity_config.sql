CREATE TABLE `billing_entity_config` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `hierarchy_type` varchar(20) NOT NULL,
  `effective_date` date NOT NULL,
  `post_method` varchar(20) DEFAULT NULL,
  `plan_billing_method` varchar(20) DEFAULT NULL,
  `invoice_method` varchar(20) DEFAULT NULL,
  `settlement_method` varchar(20) DEFAULT NULL,
  `seasonal_rule_set_uuid` varchar(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_entity_config_key1` (`uuid`),
  UNIQUE KEY `billing_entity_config_key2` (`billing_entity_uuid`,`hierarchy_type`,`effective_date`),
  UNIQUE KEY `billing_entity_config_key3` (`seasonal_rule_set_uuid`,`billing_entity_uuid`,`hierarchy_type`,`effective_date`,`id`)
);