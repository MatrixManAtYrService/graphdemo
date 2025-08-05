CREATE TABLE `fee_ytd` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `year` smallint NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `currency` char(3) NOT NULL,
  `total_period_units` decimal(12,4) NOT NULL DEFAULT '0.0000',
  `total_basis_amount` decimal(12,3) NOT NULL DEFAULT '0.000',
  `total_fee_amount` decimal(12,3) NOT NULL DEFAULT '0.000',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_ytd_key1` (`uuid`),
  UNIQUE KEY `fee_ytd_key2` (`billing_entity_uuid`,`year`,`fee_category`,`fee_code`,`currency`)
);