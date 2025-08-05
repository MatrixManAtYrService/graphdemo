CREATE TABLE `processing_note_mutation` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mutation_action` enum('UPDATE','DELETE') NOT NULL,
  `mutation_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `processing_note_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) DEFAULT NULL,
  `process_date` date DEFAULT NULL,
  `note_code` varchar(25) DEFAULT NULL,
  `notes` varchar(512) DEFAULT NULL,
  `request_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `processing_note_mutation_key1` (`uuid`,`id`)
);