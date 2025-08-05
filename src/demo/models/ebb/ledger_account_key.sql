CREATE TABLE `ledger_account_key` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `ledger_account_key` varchar(32) NOT NULL,
  `ledger_account_type` enum('ASSET','LIABILITY','EQUITY','REVENUE','EXPENSE') NOT NULL,
  `default_gl_code` varchar(40) DEFAULT NULL,
  `short_desc` varchar(40) NOT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_key_key1` (`uuid`),
  UNIQUE KEY `ledger_account_key_key2` (`ledger_account_key`)
);