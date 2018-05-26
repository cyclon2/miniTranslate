except_words =  [
    "a", "and", "at", "an", "as", "are", "american", "america", "about",
    "be", "by", "been", "because",
    "can", "could",
    "do", "done", "did",
    "for", "from",
    "his", "him", "her", "he", "how",
    "it", "its", "is","if", "in", "i",
    "like", "less",
    "not", "now", 
    "should", "shall", "she", 
    "just", 
    "korean", "korea", 
    "us", "upon", "up",
    "than", "the", "to", "thing", "two", "this", "that", "those", "these", "them", "they", "their",
    "out", "one", "or", "on", "our", "of", "own", "once",
    "when", "where", "which", "with", "without","what", "within", "will", "we", "would", "why",
    "your", "you", 
    "'s", "s",
]

import pymysql
from db.setting import *

def words_count(word_list):
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )
    