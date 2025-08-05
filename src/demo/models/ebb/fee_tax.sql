CREATE TABLE `fee_tax` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `fee_summary_uuid` char(26) NOT NULL,
  `tax1_amount` decimal(12,3) DEFAULT NULL,
  `tax2_amount` decimal(12,3) DEFAULT NULL,
  `tax3_amount` decimal(12,3) DEFAULT NULL,
  `tax4_amount` decimal(12,3) DEFAULT NULL,
  `tax1_rate` decimal(7,4) DEFAULT NULL,
  `tax2_rate` decimal(7,4) DEFAULT NULL,
  `tax3_rate` decimal(7,4) DEFAULT NULL,
  `tax4_rate` decimal(7,4) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_tax_key1` (`uuid`),
  UNIQUE KEY `fee_tax_key2` (`fee_summary_uuid`)
);