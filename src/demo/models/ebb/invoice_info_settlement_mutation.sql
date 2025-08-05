CREATE TABLE `invoice_info_settlement_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `invoice_info_settlement_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `invoice_info_uuid` varchar(26) DEFAULT NULL,
  `settlement_uuid` varchar(26) DEFAULT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_info_settlement_mutation_key1` (`uuid`,`id`)
);