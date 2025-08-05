CREATE TABLE `lexi_attribute` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `word` varchar(512) NOT NULL,
  `lexicon` varchar(128) NOT NULL,
  `attr_name` varchar(128) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `deleted_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `lexicon_word` (`lexicon`,`word`)
);