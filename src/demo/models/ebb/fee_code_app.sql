CREATE TABLE `fee_code_app` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `developer_uuid` char(13) NOT NULL,
  `developer_app_uuid` varchar(13) DEFAULT NULL,
  `app_subscription_uuid` varchar(13) DEFAULT NULL,
  `app_metered_uuid` varchar(13) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `fee_code_app_key1` (`uuid`),
  UNIQUE KEY `fee_code_app_key2` (`fee_category`,`fee_code`),
  UNIQUE KEY `fee_code_app_key3` (`developer_app_uuid`,`app_subscription_uuid`,`fee_category`,`fee_code`),
  UNIQUE KEY `fee_code_app_key4` (`developer_app_uuid`,`app_metered_uuid`,`fee_category`,`fee_code`),
  KEY `fee_code_app_key5` (`developer_uuid`,`developer_app_uuid`,`fee_category`,`fee_code`)
);