CREATE TABLE `jobrunr_jobs` (
`id` char(36) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `version` int NOT NULL,
  `jobAsJson` mediumtext COLLATE utf8mb3_bin,
  `jobSignature` varchar(512) COLLATE utf8mb3_bin NOT NULL,
  `state` varchar(36) COLLATE utf8mb3_bin NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `scheduledAt` datetime(6) DEFAULT NULL,
  `recurringJobId` varchar(128) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `jobrunr_state_idx` (`state`),
  KEY `jobrunr_job_signature_idx` (`jobSignature`),
  KEY `jobrunr_job_created_at_idx` (`createdAt`),
  KEY `jobrunr_job_scheduled_at_idx` (`scheduledAt`),
  KEY `jobrunr_job_rci_idx` (`recurringJobId`),
  KEY `jobrunr_jobs_state_updated_idx` (`state`,`updatedAt`)
);