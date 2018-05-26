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

INSERT INTO `User` (`userid`, `password`) VALUES('admin', 'admin');
INSERT INTO `User` (`userid`, `password`) VALUES('asdf', 'asdf');

CREATE INDEX `user_id_index` ON `User`(`id`);

CREATE TABLE IF NOT EXISTS `Word` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `dictid` VARCHAR(32) NOT NULL,  -- daum dictionary id 
    `word` VARCHAR(32) NOT NULL,
    `meaning` VARCHAR(128),
    `ignore` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (`word`),
    PRIMARY KEY (`id`)
);
CREATE INDEX `word_id_index` ON `Word`(`id`);
INSERT INTO `Word` (`dictid`, `word`) VALUES('ekw000098168', 'live');
INSERT INTO `Word` (`dictid`, `word`) VALUES('ekw000078268', 'hello');
INSERT INTO `Word` (`dictid`, `word`) VALUES('ekw000188687', 'yellow');

CREATE TABLE IF NOT EXISTS `UserWord` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `wordid` INT(5) unsigned NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `count` INT(10) unsigned DEFAULT 0 NOT NULL,
    `like` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (wordid) REFERENCES `Word`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

INSERT INTO `UserWord` (`userid`,`wordid`) VALUES( (SELECT id FROM `User` WHERE userid='admin'), (SELECT id FROM `Word` WHERE word='live'));
INSERT INTO `UserWord` (`userid`,`wordid`) VALUES( (SELECT id FROM `User` WHERE userid='admin'), (SELECT id FROM `Word` WHERE word='yellow'));


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

INSERT INTO `Sentence` (`userid`, `raw`, `translated`) VALUES ((SELECT id FROM `User` WHERE userid='admin'), "hello", "안녕");
INSERT INTO `Sentence` (`userid`, `raw`, `translated`) VALUES ((SELECT id FROM `User` WHERE userid='admin'), "hell", "지옥");