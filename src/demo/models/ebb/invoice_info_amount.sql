CREATE TABLE `invoice_info_amount` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `invoice_info_uuid` char(26) NOT NULL,
  `currency` char(3) NOT NULL,
  `amount` decimal(12,3) NOT NULL,
  `fee_category_group` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice_info_amount_key1` (`uuid`),
  UNIQUE KEY `invoice_info_amount_key2` (`invoice_info_uuid`,`currency`,`fee_category_group`)
);