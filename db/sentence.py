from flask_restful import Resource, reqparse
from flask_login import login_required, current_user
from db.setting import *
from db.query import *
import pymysql

parser = reqparse.RequestParser()
parser.add_argument('raw', type=str)
parser.add_argument('translated', type=str)

class Sentence(Resource):
    decorators = [login_required]
    def get(self, sentenceid):
        return {'hello': current_user.user_id}

    decorators = [login_required]
    def post(self):
        args = parser.parse_args()
        raw_sentence = args['raw']
        translated_sentence = args['translated']
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute(INSERT_SENTENCE_QUERY ,(current_user.user_id, raw_sentence, translated_sentence))
        conn.commit()
        conn.close()
        return {'rusult': 'success'}

    decorators = [login_required]
    def delete(self, sentenceid):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute(DELETE_SENTENCE_QUERY % (sentenceid))
        conn.commit()
        conn.close()
        return {'rusult': 'success'}