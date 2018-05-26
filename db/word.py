
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user
import asyncio
import pymysql
from db.setting import *
from db.query import *
import sys
sys.path.append('~/translate')
from utils.dic_daum import search_rough_all, search_detail_all

parser = reqparse.RequestParser()
parser.add_argument('word', type=str)
parser.add_argument('dictid', type=str)

class Word(Resource):
    decorators = [login_required]
    def get(self):
        return {'hello': 'world'}

    decorators = [login_required]
    def post(self):
        args = parser.parse_args()
        word = args['word']
        dictid = args['dictid']
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        try:
            cursor.execute(INSERT_WORD_QUERY % (word, dictid))
            wordid = cursor.lastrowid
            conn.commit()
        except Exception as e:
            cursor.execute(SELECT_WORD_QUERY % (word))
            reselt = cursor.fetchone()
            wordid = reselt[0]
            print(wordid)
        cursor.execute(INSERT_USERWORD_QUERY % (current_user.user_id, wordid))
        conn.commit()
        conn.close()
        return {'rusult': 'success'}

    decorators = [login_required]
    def delete(self, wordid):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute(DELETE_WORD_QUERY % (wordid))
        conn.commit()
        conn.close()
        return {'rusult': 'success'}

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
    return (x[1][1].strip(), x[0])

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
