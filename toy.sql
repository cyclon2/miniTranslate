SET character_set_server = utf8;
SET character_set_database = utf8;

DROP DATABASE IF EXISTS `toy`;

CREATE DATABASE IF NOT EXISTS `toy`;

use toy;

CREATE TABLE IF NOT EXISTS `User` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` VARCHAR(32) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    `email` VARCHAR(50),
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE INDEX (`userid`)
);

CREATE INDEX `user_id_index` ON `User`(`id`);
CREATE INDEX `user_userid_index` ON `User`(`userid`);

INSERT INTO `User` (`userid`, `password`) VALUES('admin', 'admin');
INSERT INTO `User` (`userid`, `password`) VALUES('asdf', 'asdf');

CREATE TABLE IF NOT EXISTS `Word` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `dictid` VARCHAR(32) NOT NULL,  -- daum dictionary id 
    `word` VARCHAR(32) NOT NULL,
    `meaning` VARCHAR(128),
    `ignore` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE INDEX (`word`)
);

CREATE INDEX `word_id_index` ON `Word`(`id`);
CREATE INDEX `word_word_index` ON `Word`(`id`);
INSERT INTO `User` (`userid`, `password`) VALUES('admin', 'admin');


CREATE TABLE IF NOT EXISTS `UserWord` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `wordid` INT(5) unsigned NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `count` INT(10) unsigned DEFAULT 1 NOT NULL,
    `like` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (wordid) REFERENCES `Word`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`),
    UNIQUE INDEX (`wordid`)
);

CREATE TABLE IF NOT EXISTS `Sentence` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `raw` TEXT NOT NULL,
    `translated` TEXT NOT NULL,
    `like` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);
