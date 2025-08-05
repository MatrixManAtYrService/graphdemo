CREATE TABLE `adjust_reason` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `adjust_reason` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `adjust_reason_key1` (`uuid`),
  UNIQUE KEY `adjust_reason_key2` (`adjust_reason`)
);