CREATE TABLE `jobrunr_recurring_jobs` (
`id` char(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `version` int NOT NULL,
  `jobAsJson` text COLLATE utf8mb3_bin NOT NULL,
  `createdAt` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `jobrunr_recurring_job_created_at_idx` (`createdAt`)
);