CREATE TABLE `prototype_fee_rate` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `prototype_fee_set_id` bigint unsigned NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `currency` char(3) NOT NULL,
  `apply_type` enum('DEFAULT','PER_ITEM','PERCENTAGE','BOTH','NONE','FLAT') NOT NULL,
  `per_item_amount` decimal(12,3) DEFAULT NULL,
  `percentage` decimal(5,2) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `prototype_fee_rate_key1` (`uuid`),
  UNIQUE KEY `prototype_fee_rate_key2` (`prototype_fee_set_id`,`billing_entity_uuid`,`fee_category`,`fee_code`,`currency`)
);