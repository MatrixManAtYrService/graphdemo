CREATE TABLE `tiered_pricing` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `tiered_rule_uuid` char(26) NOT NULL,
  `effective_date` date NOT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tiered_pricing_key1` (`uuid`),
  UNIQUE KEY `tiered_pricing_key2` (`billing_entity_uuid`,`effective_date`,`deleted_date`,`tiered_rule_uuid`,`id`),
  UNIQUE KEY `tiered_pricing_key3` (`tiered_rule_uuid`,`billing_entity_uuid`,`effective_date`,`deleted_date`,`id`)
);