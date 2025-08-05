CREATE TABLE `invoice_info_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `invoice_info_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) DEFAULT NULL,
  `entity_uuid` char(13) DEFAULT NULL,
  `alternate_id` varchar(25) DEFAULT NULL,
  `billing_date` date DEFAULT NULL,
  `invoice_num` varchar(30) DEFAULT NULL,
  `currency` char(3) DEFAULT NULL,
  `total_amount` decimal(12,3) DEFAULT NULL,
  `document_uuid` char(26) DEFAULT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_info_mutation_key1` (`uuid`,`id`)
);