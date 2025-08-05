CREATE TABLE `ledger_account_action` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `action` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_action_key1` (`uuid`),
  UNIQUE KEY `ledger_account_action_key2` (`action`)
);