CREATE TABLE `billing_archetype` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `archetype_type` enum('MERCHANT','RESELLER','DEVELOPER','PSEUDO') NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_archetype_key1` (`uuid`),
  UNIQUE KEY `billing_archetype_key2` (`archetype_type`,`uuid`)
);