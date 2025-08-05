CREATE TABLE `jobrunr_migrations` (
`id` char(36) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `script` varchar(64) COLLATE utf8mb3_bin NOT NULL,
  `installedOn` varchar(29) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`)
);