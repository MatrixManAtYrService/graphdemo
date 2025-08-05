CREATE TABLE `billing_entity` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `entity_uuid` char(13) NOT NULL,
  `entity_type` enum('MERCHANT','RESELLER','DEVELOPER','PSEUDO','ARCHETYPE') NOT NULL,
  `name` varchar(127) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_entity_key1` (`uuid`),
  UNIQUE KEY `billing_entity_key2` (`entity_uuid`,`entity_type`)
);