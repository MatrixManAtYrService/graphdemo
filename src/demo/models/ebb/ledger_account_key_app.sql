CREATE TABLE `ledger_account_key_app` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `ledger_account_key` varchar(32) NOT NULL,
  `developer_uuid` char(13) NOT NULL,
  `developer_app_uuid` varchar(13) DEFAULT NULL,
  `app_subscription_uuid` varchar(13) DEFAULT NULL,
  `app_metered_uuid` varchar(13) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ledger_account_key_app_key1` (`uuid`),
  UNIQUE KEY `ledger_account_key_app_key2` (`ledger_account_key`),
  UNIQUE KEY `ledger_account_key_app_key3` (`developer_app_uuid`,`app_subscription_uuid`,`ledger_account_key`),
  UNIQUE KEY `ledger_account_key_app_key4` (`developer_app_uuid`,`app_metered_uuid`,`ledger_account_key`),
  KEY `ledger_account_key_app_key5` (`developer_uuid`,`developer_app_uuid`,`ledger_account_key`)
);