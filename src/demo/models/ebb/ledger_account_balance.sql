CREATE TABLE `ledger_account_balance` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `ledger_account_uuid` char(26) NOT NULL,
  `currency` char(3) NOT NULL,
  `balance` decimal(12,3) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_balance_key1` (`uuid`),
  UNIQUE KEY `ledger_account_balance_key2` (`ledger_account_uuid`,`currency`)
);