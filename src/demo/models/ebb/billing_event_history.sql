CREATE TABLE `billing_event_history` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `environment` varchar(25) NOT NULL,
  `entity_uuid` char(13) NOT NULL,
  `entity_type` enum('MERCHANT','RESELLER','DEVELOPER') NOT NULL,
  `event_uuid` varchar(26) DEFAULT NULL,
  `input` text NOT NULL,
  `message` varchar(1024) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `billing_event_history_index1` (`event_uuid`),
  KEY `billing_event_history_index2` (`entity_uuid`,`created_timestamp`)
);