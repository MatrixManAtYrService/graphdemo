CREATE TABLE `ledger_journal` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `ledger_account_uuid` char(26) NOT NULL,
  `journal_date` date NOT NULL,
  `ref_uuid_type` enum('FEE_SUMMARY','SETTLE_EXPORT','SETTLE_IMPORT','FEE_TAX') NOT NULL,
  `ref_uuid` char(26) NOT NULL,
  `cr_db` enum('CREDIT','DEBIT') NOT NULL,
  `currency` char(3) NOT NULL,
  `amount` decimal(12,3) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_journal_key1` (`uuid`),
  UNIQUE KEY `ledger_journal_key3` (`ref_uuid_type`,`ref_uuid`,`id`),
  UNIQUE KEY `ledger_journal_key2` (`ledger_account_uuid`,`journal_date`,`id`)
);