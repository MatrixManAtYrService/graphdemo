CREATE TABLE `deserializable_failure` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `topic` varchar(127) NOT NULL,
  `channel` varchar(127) NOT NULL,
  `b64` text NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `deserializable_failure_index1` (`uuid`)
);