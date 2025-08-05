CREATE TABLE `fee_tax_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `fee_tax_id` bigint unsigned NOT NULL,
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
  UNIQUE KEY `fee_tax_mutation_key1` (`uuid`,`id`)
);