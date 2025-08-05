CREATE TABLE `billing_hierarchy` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `hierarchy_type` varchar(20) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `effective_date` date NOT NULL,
  `deleted_date` date DEFAULT NULL,
  `parent_billing_hierarchy_uuid` varchar(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_hierarchy_key1` (`uuid`),
  UNIQUE KEY `billing_hierarchy_key2` (`hierarchy_type`,`billing_entity_uuid`,`effective_date`),
  KEY `billing_hierarchy_key3` (`hierarchy_type`,`parent_billing_hierarchy_uuid`,`id`)
);