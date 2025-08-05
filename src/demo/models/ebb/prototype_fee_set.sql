CREATE TABLE `prototype_fee_set` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `name` varchar(40) NOT NULL,
  `disposition` enum('DRAFT','PROMOTED','REMOVED') NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `effective_date` date NOT NULL,
  `disposition_datetime` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `prototype_fee_set_key1` (`uuid`)
);