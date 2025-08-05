CREATE TABLE `look` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(32) NOT NULL,
  `hash` char(64) NOT NULL,
  `namespace` varchar(32) NOT NULL,
  `metadata` varchar(1024) DEFAULT NULL,
  `processed_timestamp` datetime(6) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `namespace_hash` (`namespace`,`hash`)
);