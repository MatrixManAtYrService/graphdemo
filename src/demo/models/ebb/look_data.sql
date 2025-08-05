CREATE TABLE `look_data` (
`id` int unsigned NOT NULL AUTO_INCREMENT,
  `look_uuid` char(32) NOT NULL,
  `payload` blob NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `look_uuid` (`look_uuid`)
);