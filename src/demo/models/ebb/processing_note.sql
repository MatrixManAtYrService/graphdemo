CREATE TABLE `processing_note` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `process_date` date DEFAULT NULL,
  `note_code` varchar(25) NOT NULL,
  `notes` varchar(512) DEFAULT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `processing_note_key1` (`uuid`),
  UNIQUE KEY `processing_note_key2` (`billing_entity_uuid`,`process_date`,`uuid`),
  UNIQUE KEY `processing_note_key3` (`request_uuid`,`billing_entity_uuid`,`uuid`)
);