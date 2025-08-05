CREATE TABLE `fee_code` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `short_desc` varchar(40) NOT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `sort_order` int NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_code_key1` (`uuid`),
  UNIQUE KEY `fee_code_key2` (`fee_category`,`fee_code`)
);