CREATE TABLE `lexi_rule` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `parent_uuid` char(36) DEFAULT NULL,
  `lexicon` varchar(128) NOT NULL,
  `rule_name` varchar(128) NOT NULL,
  `description` varchar(512) DEFAULT NULL,
  `rule_condition` varchar(512) DEFAULT NULL,
  `target_attributes` varchar(512) DEFAULT NULL,
  `priority` int DEFAULT '1',
  `rule_type` enum('SIMPLE','UNIT','ACTIVATION','CONDITIONAL') NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `deleted_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `lexicon_name` (`lexicon`,`rule_name`)
);