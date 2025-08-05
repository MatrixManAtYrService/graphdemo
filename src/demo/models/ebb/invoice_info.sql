CREATE TABLE `invoice_info` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `entity_uuid` char(13) DEFAULT NULL,
  `alternate_id` varchar(25) DEFAULT NULL,
  `billing_date` date NOT NULL,
  `invoice_num` varchar(30) NOT NULL,
  `currency` char(3) NOT NULL,
  `total_amount` decimal(12,3) NOT NULL,
  `document_uuid` char(26) DEFAULT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice_key1` (`uuid`),
  UNIQUE KEY `invoice_key2` (`billing_entity_uuid`,`billing_date` DESC,`id`),
  UNIQUE KEY `invoice_key3` (`invoice_num`,`billing_date` DESC,`id`),
  UNIQUE KEY `invoice_info_key4` (`request_uuid`,`billing_entity_uuid`,`id`)
);