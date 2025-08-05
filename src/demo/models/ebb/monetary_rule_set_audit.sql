CREATE TABLE `monetary_rule_set_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `monetary_rule_set_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `rule_status` enum('SETUP','ACTIVE','DEPRECATED','DELETED') DEFAULT NULL,
  `short_desc` varchar(40) DEFAULT NULL,
  `full_desc` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_rule_set_audit_key1` (`uuid`,`id`)
);