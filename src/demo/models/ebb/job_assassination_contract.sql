CREATE TABLE `job_assassination_contract` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `job_identifier` varchar(50) NOT NULL,
  `killed` smallint NOT NULL DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `job_assassination_contract_key1` (`job_identifier`,`id`)
);