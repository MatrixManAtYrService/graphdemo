CREATE TABLE `jobrunr_metadata` (
`id` varchar(156) COLLATE utf8mb3_bin NOT NULL,
  `name` varchar(92) COLLATE utf8mb3_bin NOT NULL,
  `owner` varchar(64) COLLATE utf8mb3_bin NOT NULL,
  `value` text COLLATE utf8mb3_bin NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
);