DROP DATABASE IF EXISTS `toy`;

CREATE DATABASE IF NOT EXISTS `toy`;

use toy;

CREATE TABLE IF NOT EXISTS `user` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` VARCHAR(32) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    `email` VARCHAR(50),
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

INSERT INTO `user` (`userid`, `password`) VALUES('admin', 'admin');

CREATE TABLE IF NOT EXISTS `word` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` VARCHAR(32) NOT NULL,
    `dictid` VARCHAR(32) NOT NULL,
    `word` VARCHAR(32) NOT NULL,
    `count` INT(10) unsigned DEFAULT 0 NOT NULL,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `favorite_word` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `dictid` VARCHAR(32) NOT NULL,
    `userid` VARCHAR(32) NOT NULL,
    `word` VARCHAR(32) NOT NULL,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);