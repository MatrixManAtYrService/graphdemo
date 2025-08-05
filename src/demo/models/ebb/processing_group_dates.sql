CREATE TABLE `processing_group_dates` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `hierarchy_type` varchar(20) NOT NULL,
  `cycle_date` date NOT NULL,
  `last_cycle_date` date DEFAULT NULL,
  `posting_date` date NOT NULL,
  `last_posting_date` date DEFAULT NULL,
  `billing_date` date NOT NULL,
  `last_billing_date` date DEFAULT NULL,
  `settlement_date` date NOT NULL,
  `last_settlement_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `processing_group_dates_key1` (`uuid`),
  UNIQUE KEY `processing_group_dates_key2` (`billing_entity_uuid`,`hierarchy_type`)
);