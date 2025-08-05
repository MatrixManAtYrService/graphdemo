CREATE TABLE `revenue_share_group` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `revenue_share_group` varchar(20) NOT NULL,
  `short_desc` varchar(40) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `revenue_share_group_key1` (`uuid`),
  UNIQUE KEY `revenue_share_group_key2` (`revenue_share_group`)
);