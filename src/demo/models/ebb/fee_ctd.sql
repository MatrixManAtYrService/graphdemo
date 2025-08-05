CREATE TABLE `fee_ctd` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `currency` char(3) NOT NULL,
  `ctd_num_units` decimal(12,4) NOT NULL DEFAULT '0.0000',
  `abs_num_units` decimal(12,4) NOT NULL DEFAULT '0.0000',
  `ctd_basis_amount` decimal(12,3) NOT NULL DEFAULT '0.000',
  `abs_basis_amount` decimal(12,3) NOT NULL DEFAULT '0.000',
  `num_actions` int NOT NULL DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_ctd_key1` (`uuid`),
  UNIQUE KEY `fee_ctd_key2` (`billing_entity_uuid`,`fee_category`,`fee_code`,`currency`)
);