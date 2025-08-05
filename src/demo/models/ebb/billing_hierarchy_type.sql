CREATE TABLE `billing_hierarchy_type` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `hierarchy_type` varchar(20) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_hierarchy_type_key1` (`uuid`),
  UNIQUE KEY `billing_hierarchy_type_key2` (`hierarchy_type`)
);