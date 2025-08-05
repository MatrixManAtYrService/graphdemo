CREATE TABLE `misc_specifier` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `misc_specifier` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `misc_specifier_key1` (`uuid`),
  UNIQUE KEY `misc_specifier_key2` (`misc_specifier`)
);