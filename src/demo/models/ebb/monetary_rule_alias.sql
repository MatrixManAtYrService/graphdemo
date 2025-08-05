CREATE TABLE `monetary_rule_alias` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `rule_alias` varchar(25) NOT NULL,
  `rule_type` enum('AUTO_ADJUST','TIERED') NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `monetary_rule_alias_key1` (`uuid`),
  UNIQUE KEY `monetary_rule_alias_key2` (`rule_alias`,`rule_type`)
);