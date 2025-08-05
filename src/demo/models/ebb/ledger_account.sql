CREATE TABLE `ledger_account` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `ledger_account_key` varchar(32) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `gl_code` varchar(40) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_key1` (`uuid`),
  UNIQUE KEY `ledger_account_key2` (`ledger_account_key`,`billing_entity_uuid`),
  UNIQUE KEY `ledger_account_key3` (`billing_entity_uuid`,`ledger_account_key`)
);