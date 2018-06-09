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
    `type` INT(1) NOT NULL DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE INDEX (`userid`)
);

CREATE TABLE IF NOT EXISTS `UserInfo` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
	`main_page` VARCHAR(50) NOT NULL DEFAULT "tr",
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

CREATE TABLE IF NOT EXISTS `Neighbor` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
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
CREATE INDEX `word_word_index` ON `Word`(`word`);

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

CREATE TABLE IF NOT EXISTS `Book` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `title` VARCHAR(32) NOT NULL,
    `color` char(6) NOT NULL,
    `summary` TEXT NOT NULL,
    `open` BOOLEAN DEFAULT 1,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

INSERT into `Book` (`userid`, `title`, `color`, `summary`) VALUES (1, "안녕하세요.", "001100", "테스트페이지");
INSERT into `Book` (`userid`, `title`, `color`, `summary`) VALUES (1, "안녕하세요.", "001100", "테스트페이지");

CREATE TABLE IF NOT EXISTS `Post` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `bookid` INT(5) unsigned,
    `title` VARCHAR(32) NOT NULL,
    `content` TEXT NOT NULL,
    `open` BOOLEAN DEFAULT 1,
    `visit` INT(5) unsigned NOT NULL DEFAULT 0,
    `nocomment` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (bookid) REFERENCES `Book`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

INSERT into `Post` (`userid`, `bookid`, `title`, `content`) VALUES (1,1, "안녕하세요.","테스트페이지");
INSERT into `Post` (`userid`, `bookid`, `title`, `content`) VALUES (1,1, "안녕하세요22.","<p><strong>Unwilling sportsmen he in questions september therefore described so. Attacks may set few believe moments was. Reasonably how possession shy way introduced age inquietude. Missed he engage no exeter of. Still tried means we aware order among on. Eldest father can design tastes did joy settle. Roused future he ye an marked. Arose mr rapid in so vexed words. Gay welcome led add lasting chiefly say looking.&nbsp;</strong></p><p><br></p><p>He my polite be object oh change. Consider no mr am overcame yourself throwing sociable children. Hastily her totally conduct may. My solid by stuff first smile fanny. Humoured how advanced mrs elegance sir who. Home sons when them dine do want to. Estimating themselves unsatiable imprudence an he at an. Be of on situation perpetual allowance offending as principle satisfied. Improved carriage securing are desirous too.&nbsp;</p><p><br></p><p><strong>Do to be agreeable conveying oh assurance. Wicket longer admire do barton vanity itself do in it. Preferred to sportsmen it engrossed listening. Park gate sell they west hard for the. Abode stuff noisy manor blush yet the far. Up colonel so between removed so do. Years use place decay sex worth drift age. Men lasting out end article express fortune demands own charmed. About are are money ask how seven.&nbsp;</strong></p><p><br></p><p>Wrote water woman of heart it total other. By in entirely securing suitable graceful at families improved. Zealously few furniture repulsive was agreeable consisted difficult. Collected breakfast estimable questions in to favourite it. Known he place worth words it as to. Spoke now noise off smart her ready.&nbsp;</p><p><br></p><p><u>Considered an invitation do introduced sufficient understood instrument it. Of decisively friendship in as collecting at. No affixed be husband ye females brother garrets proceed. Least child who seven happy yet balls young. Discovery sweetness principle discourse shameless bed one excellent. Sentiments of surrounded friendship dispatched connection is he. Me or produce besides hastily up as pleased. Bore less when had and john shed hope.&nbsp;</u></p><p><br></p><p>And produce say the ten moments parties. Simple innate summer fat appear basket his desire joy. Outward clothes promise at gravity do excited. Sufficient particular impossible by reasonable oh expression is. Yet preference connection unpleasant yet melancholy but end appearance. And excellence partiality estimating terminated day everything.&nbsp;</p><p><br></p><p>Questions explained agreeable preferred strangers too him her son. Set put shyness offices his females him distant. Improve has message besides shy himself cheered however how son. Quick judge other leave ask first chief her. Indeed or remark always silent seemed narrow be. Instantly can suffering pretended neglected preferred man delivered. Perhaps fertile brandon do imagine to cordial cottage.&nbsp;</p><p><br></p><p>Whether article spirits new her covered hastily sitting her. Money witty books nor son add. Chicken age had evening believe but proceed pretend mrs. At missed advice my it no sister. Miss told ham dull knew see she spot near can. Spirit her entire her called.&nbsp;</p><p><br></p><p>Oh he decisively impression attachment friendship so if everything. Whose her enjoy chief new young. Felicity if ye required likewise so doubtful. On so attention necessary at by provision otherwise existence direction. Unpleasing up announcing unpleasant themselves oh do on. Way advantage age led listening belonging supposing.&nbsp;</p><p><br></p><p>Delightful unreserved impossible few estimating men favourable see entreaties. She propriety immediate was improving. He or entrance humoured likewise moderate. Much nor game son say feel. Fat make met can must form into gate. Me we offending prevailed discovery.&nbsp;</p><p><br></p>");


CREATE TABLE IF NOT EXISTS `UserLikePost` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `postid` INT(5) unsigned NOT NULL,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (postid) REFERENCES `Post`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

CREATE TABLE IF NOT EXISTS `Comment` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `postid` INT(5) unsigned NOT NULL,
    `comment` VARCHAR(200) NOT NULL,
    `open` BOOLEAN DEFAULT 1,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (postid) REFERENCES `Post`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

CREATE TABLE IF NOT EXISTS `MemoCategory` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `title` VARCHAR(32) NOT NULL,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);

CREATE TABLE IF NOT EXISTS `Memo` (
    `id` INT(5) unsigned AUTO_INCREMENT NOT NULL,
    `userid` INT(5) unsigned NOT NULL,
    `categoryid` INT(5) unsigned NOT NULL,
    `content` VARCHAR(200) NOT NULL,
    `open` BOOLEAN DEFAULT 1,
    `like` BOOLEAN DEFAULT 0,
    `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (categoryid) REFERENCES `MemoCategory`(`id`),
    FOREIGN KEY (userid) REFERENCES `User`(`id`)
);
