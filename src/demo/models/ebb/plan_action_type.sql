CREATE TABLE `plan_action_type` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `plan_action_type` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `plan_action_type_key1` (`uuid`),
  UNIQUE KEY `plan_action_type_key2` (`plan_action_type`)
);