CREATE TABLE `tiered_rule_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `tiered_rule_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `rule_status` enum('SETUP','ACTIVE','DEPRECATED','DELETED') NOT NULL DEFAULT 'SETUP',
  `tiered_basis` enum('QUANTITY','VOLUME','BOTH') NOT NULL,
  `tiered_model` enum('APPLY_TO_TIER','APPLY_TO_ALL') NOT NULL,
  `target_entity_type` enum('MERCHANT','RESELLER','DEVELOPER') NOT NULL,
  `short_desc` varchar(40) NOT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tiered_rule_audit_key1` (`uuid`,`id`)
);