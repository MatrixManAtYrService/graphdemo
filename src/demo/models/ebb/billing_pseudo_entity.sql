CREATE TABLE `billing_pseudo_entity` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `name` varchar(127) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_pseudo_entity_key1` (`uuid`)
);