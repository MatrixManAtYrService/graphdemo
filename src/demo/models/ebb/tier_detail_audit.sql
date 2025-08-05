CREATE TABLE `tier_detail_audit` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `audit_action` enum('UPDATE','DELETE') NOT NULL,
  `audit_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `tier_detail_id` bigint unsigned NOT NULL,
  `uuid` char(26) NOT NULL,
  `tiered_rule_uuid` char(26) NOT NULL,
  `min_units` decimal(12,4) DEFAULT NULL,
  `min_amount` decimal(12,3) DEFAULT NULL,
  `currency` varchar(3) DEFAULT NULL,
  `rate_fee_category` varchar(25) NOT NULL,
  `rate_fee_code` varchar(25) NOT NULL,
  `short_desc` varchar(40) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tier_detail_audit_key1` (`uuid`,`id`)
);