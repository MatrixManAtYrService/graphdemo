CREATE TABLE `monetary_rule_set` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `rule_status` enum('SETUP','ACTIVE','DEPRECATED','DELETED') NOT NULL DEFAULT 'SETUP',
  `short_desc` varchar(40) NOT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_rule_set_key1` (`uuid`),
  UNIQUE KEY `monetary_rule_set_key2` (`rule_status`,`uuid`,`id`)
);