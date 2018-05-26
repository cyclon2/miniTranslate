except_words =  [
    "a", "and", "at", "an", "as", "are", "american", "america", "about", "although",
    "be", "by", "been", "because", "but",
    "can", "could",
    "do", "done", "did",
    "for", "from",
    "his", "him", "her", "he", "how", "has",
    "it", "its", "is","if", "in", "i",
    "like", "less",
    "not", "now", 
    "should", "shall", "she", 
    "just", 
    "korean", "korea", 
    "us", "upon", "up",
    "than", "the", "to", "thing", "two", "this", "that", "those", "these", "them", "they", "their", "true", "then",
    "out", "one", "or", "on", "our", "of", "own", "once",
    "when", "where", "which", "with", "without","what", "within", "will", "we", "would", "why",
    "your", "you", 
    "'s", "s", "so", "such", "size",
]

def except_check(w):
    if w.lower() not in except_words:
        return True
    return False

import pymysql
from db.setting import *

def words_count(word_list):
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )
    