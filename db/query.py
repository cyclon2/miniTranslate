WORD_QUERY = "SELECT w.dictid, w.word, w.meaning, uw.count, uw.like, uw.created_time FROM `UserWord` uw LEFT JOIN `Word` w ON uw.wordid = w.id WHERE uw.userid = (SELECT id FROM `User` WHERE userid='%s');"
SENTENCE_QUERY = "SELECT s.raw, s.translated, s.like, s.updated_time FROM `Sentence` s where s.userid = (SELECT id FROM `User` WHERE userid='%s');"
NO_MEANING_WORDS_QUERY = "SELECT word FROM `Word` WHERE `meaning` is NULL"
UPDATE_MEANING_QUERY = "UPDATE `Word` set `meaning`=%s WHERE `word`=%s"