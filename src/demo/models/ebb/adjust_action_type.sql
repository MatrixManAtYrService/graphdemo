CREATE TABLE `adjust_action_type` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `adjust_action_type` varchar(25) NOT NULL,
  `fee_category_group` varchar(25) NOT NULL,
  `revenue_group` varchar(25) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `adjust_action_type_key1` (`uuid`),
  UNIQUE KEY `adjust_action_type_key2` (`adjust_action_type`),
  UNIQUE KEY `adjust_action_type_key3` (`fee_category_group`,`revenue_group`)
);