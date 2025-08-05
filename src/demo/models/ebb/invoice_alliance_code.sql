CREATE TABLE `invoice_alliance_code` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `alliance_code` char(3) NOT NULL,
  `invoice_count` bigint unsigned NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice_alliance_code_key1` (`uuid`),
  UNIQUE KEY `invoice_alliance_code_key2` (`billing_entity_uuid`),
  UNIQUE KEY `invoice_alliance_code_key3` (`alliance_code`)
);