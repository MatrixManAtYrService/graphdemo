CREATE TABLE `ledger_account_key_purpose_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `ledger_account_key_purpose_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `purpose` varchar(25) DEFAULT NULL,
  `ledger_account_key` varchar(32) DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ledger_account_key_purpose_audit_key1` (`uuid`,`id`)
);