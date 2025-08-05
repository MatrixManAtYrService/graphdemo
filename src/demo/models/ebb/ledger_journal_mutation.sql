CREATE TABLE `ledger_journal_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `ledger_journal_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `ledger_account_uuid` char(26) DEFAULT NULL,
  `journal_date` date DEFAULT NULL,
  `ref_uuid_type` enum('FEE_SUMMARY','SETTLE_EXPORT','SETTLE_IMPORT','FEE_TAX') DEFAULT NULL,
  `ref_uuid` char(26) DEFAULT NULL,
  `cr_db` enum('CREDIT','DEBIT') DEFAULT NULL,
  `currency` char(3) DEFAULT NULL,
  `amount` decimal(12,3) DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ledger_journal_mutation_key1` (`uuid`,`id`)
);