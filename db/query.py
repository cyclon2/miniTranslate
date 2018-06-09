## UserWord
UPDATE_WORD_COUNT_QUERY = "UPDATE `UserWord` set `count`= `count`+1 WHERE `wordid`=(SELECT `id` FROM `Word` WHERE `word`='%s') and `userid`=(SELECT id FROM `User` WHERE userid='%s')"
UPDATE_USERWORD_LIKE_QUERY="UPDATE `UserWord` set `like`=1 WHERE `wordid`=(SELECT `id` FROM `Word` WHERE `word`='%s')"
INSERT_USERWORD_QUERY = "INSERT INTO `UserWord`(`userid`, `wordid`) VALUES ((SELECT id FROM `User` WHERE userid='%s'), %s)"
INSERT_USERWORD_QUERY2 = "INSERT INTO `UserWord`(`userid`, `wordid`) VALUES ((SELECT id FROM `User` WHERE userid='%s'), (SELECT `id` FROM `Word` WHERE `word`='%s'))"
DELETE_USERWORD_QUERY="DELETE FROM `UserWord` WHERE `id`=%s;"
USERWORD_QUERY = "SELECT w.dictid, w.word, w.meaning, uw.count FROM `UserWord` uw LEFT JOIN `Word` w ON uw.wordid = w.id WHERE uw.userid = (SELECT id FROM `User` WHERE userid='%s') order by uw.count DESC limit 30;"

## User
USERWORD_LIKE_QUERY = "SELECT w.dictid, w.word, w.meaning, uw.count, uw.like, uw.created_time, uw.id FROM `UserWord` uw LEFT JOIN `Word` w ON uw.wordid = w.id WHERE uw.like=1 and uw.userid = (SELECT id FROM `User` WHERE userid='%s');"
SENTENCE_QUERY = "SELECT s.raw, s.translated, s.like, s.updated_time, s.id FROM `Sentence` s where s.userid = (SELECT id FROM `User` WHERE userid='%s');"
DELETE_SENTENCE_QUERY="DELETE FROM `Sentence` WHERE `id`=%s;"

## Word
SELECT_WORD_QUERY = "SELECT id FROM `Word` WHERE `word`='%s'"
SELECT_IGNORE_WORD_QUERY_ALL = """SELECT * FROM `Word` WHERE `word`='%s' and `ignore`=1"""
SELECT_WORD_QUERY_ALL = """SELECT * FROM `Word` WHERE `word`='%s'"""
NO_MEANING_WORDS_QUERY = "SELECT word FROM `Word` WHERE `meaning` is NULL"
UPDATE_MEANING_QUERY = "UPDATE `Word` set `meaning`=%s WHERE `word`=%s"
INSERT_SENTENCE_QUERY="""INSERT INTO `Sentence` (`userid`, `raw`, `translated`) VALUES ((SELECT id FROM `User` WHERE userid=%s), %s, %s);"""
INSERT_WORD_QUERY = "INSERT INTO `Word`(`word`, `dictid`) VALUES ('%s', '%s')"
INSERT_WORD_QUERY_MEANING = "INSERT INTO `Word`(`word`, `dictid`, `meaning`) VALUES ('%s', '%s', '%s')"

## Book
SELECT_BOOK_QUERY = """SELECT * FROM `Book` WHERE `userid`=(SELECT id FROM `User` WHERE userid=%s)"""

## Post
SELECT_POST_BOOKID_QUERY = """SELECT * FROM `Post` WHERE `bookid`=%s and `userid`=(SELECT id FROM `User` WHERE userid=%s)"""
SELECT_POSTS_QUERY = """SELECT id, title, content, updated_time FROM `Post` WHERE `userid`=(SELECT id FROM `User` WHERE `userid`='%s') ORDER BY `updated_time` DESC """
INSERT_POST_QUERY = """INSERT into `Post` (`userid`, `bookid`, `title`, `content`) VALUES ((SELECT id FROM `User` WHERE `userid`='%s'), (SELECT id FROM `Book` WHERE `title`='%s'), "%s","%s")"""
SELECT_POST_QUERY = """SELECT title, content, updated_time, (SELECT userid from User where p.userid=id) FROM `Post` p WHERE `id`=%s"""

##`userid`=(SELECT id FROM `User` WHERE `userid`='%s') and 
