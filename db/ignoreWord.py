from flask_restful import Resource, reqparse
from flask_login import login_required, current_user
import asyncio
import pymysql
from db.setting import *
from db.Query import *
import sys
sys.path.append('~/translate')
from utils.dic_daum import search_rough_all, search_detail_all
from utils.word import *

parser = reqparse.RequestParser()
parser.add_argument('word', type=str)
parser.add_argument('dictid', type=str)

class IgnoredWord(Resource):
    decorators = [login_required]
    def get(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        conn.close()
        return {'data' :data}

    decorators = [login_required]
    def patch(self): # ignore toggle
        args = parser.parse_args()
        word = args['word']
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        conn.commit()
        conn.close()
        return {'rusult': 'success'}

class ignoredWord:
    def get_words(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
         cursor.execute(USERWORD_IGNORE_QUERY % (self.user_id))
        conn.close()
        return  info   
    