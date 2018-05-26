
import pymysql
from setting import *
from query import *
import asyncio
# from ..utils.dic_daum import search_rough_all, search_detail_all
import sys
sys.path.append('/toy')
from utils.dic_daum import search_rough_all, search_detail_all

def words_count(word_list):
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )

def get_no_meanings_word():
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )
    cursor = conn.cursor()
    cursor.execute(NO_MEANING_WORDS_QUERY)
    conn.close()
    l = []
    for r in cursor.fetchall():
        l.append(r[0])
    return l

def reformatlist(x):
    return (x[1].strip(), x[0])

def set_meaning_db(words_meaning_list):
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )
    cursor = conn.cursor()
    words_meaning_list = list(map(reformatlist, words_meaning_list))
    cursor.executemany(UPDATE_MEANING_QUERY,words_meaning_list)
    conn.commit()
    conn.close()

# background work #
def set_meaning_all():
    word_list = get_no_meanings_word()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    words_meaning = loop.run_until_complete(search_rough_all(word_list))
    loop.close()
    set_meaning_db(words_meaning)