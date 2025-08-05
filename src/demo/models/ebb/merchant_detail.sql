CREATE TABLE `merchant_detail` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `seasonal` smallint NOT NULL DEFAULT '0' COMMENT 'Indicates that the merchant is a seasonal merchant (non-zero/true), or that merchant does business all year (0/false)',
  `tax_exempt` smallint NOT NULL DEFAULT '0' COMMENT 'Indicates that merchant is exempt from paying taxes (non-zero/true), or that merchant is subject to taxes (0/false)',
  `verified_terms_acceptance` smallint NOT NULL DEFAULT '0' COMMENT 'Indicates that billing terms acceptance has been verified (non-zero/true), or that terms acceptance needs to be checked/verified (0/false)',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchant_detail_key1` (`uuid`),
  UNIQUE KEY `merchant_detail_key2` (`billing_entity_uuid`)
);