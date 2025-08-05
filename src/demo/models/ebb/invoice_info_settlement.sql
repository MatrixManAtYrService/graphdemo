CREATE TABLE `invoice_info_settlement` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `invoice_info_uuid` varchar(26) NOT NULL,
  `settlement_uuid` varchar(26) NOT NULL,
  `request_uuid` char(26) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice_info_settlement_key1` (`uuid`),
  UNIQUE KEY `invoice_info_settlement_key2` (`invoice_info_uuid`,`settlement_uuid`),
  UNIQUE KEY `invoice_info_settlement_key3` (`settlement_uuid`,`invoice_info_uuid`),
  UNIQUE KEY `invoice_info_settlement_key4` (`request_uuid`,`settlement_uuid`,`invoice_info_uuid`)
);