CREATE TABLE `ledger_account_key_purpose` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `purpose` varchar(25) NOT NULL,
  `ledger_account_key` varchar(32) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_key_purpose_key1` (`uuid`),
  UNIQUE KEY `ledger_account_key_purpose_key2` (`purpose`,`ledger_account_key`),
  UNIQUE KEY `ledger_account_key_purpose_key3` (`ledger_account_key`,`purpose`)
);