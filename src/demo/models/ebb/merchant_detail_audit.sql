CREATE TABLE `merchant_detail_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `merchant_detail_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) DEFAULT NULL,
  `seasonal` smallint NOT NULL DEFAULT '0',
  `tax_exempt` smallint NOT NULL DEFAULT '0',
  `verified_terms_acceptance` smallint NOT NULL DEFAULT '0',
  `created_timestamp` datetime(6) DEFAULT NULL,
  `modified_timestamp` datetime(6) DEFAULT NULL,
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `merchant_detail_audit_key1` (`uuid`,`id`)
);