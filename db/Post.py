from flask_restful import Resource, reqparse
from flask_login import login_required, current_user
import pymysql
from db.setting import *
from db.Query import *
import sys

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('content', type=str)
parser.add_argument('book_title', type=str)

class PostApi(Resource):
    def get(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        return

    decorators = [login_required]
    def patch(self):
        return

    decorators = [login_required]
    def delete(self, wordid):
        return

    decorators = [login_required]
    def post(self):
        args = parser.parse_args()
        title = args['title']
        content = args['content']
        book_title = args['book_title']
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute(INSERT_POST_QUERY % (current_user.user_id, book_title , title, content ))
        conn.commit()
        conn.close()
        return {"result":"success"}

class Post:
    def __init__(self, id=-1, title="", content="", updated_time="", writer=""):
        if id != -1:
            conn = pymysql.connect(host=DB_HOST, 
                user=DB_USER, password=DB_PASSWORD,
                db='toy', charset='utf8'
            )
            cursor = conn.cursor()
            cursor.execute(SELECT_POST_QUERY % (id ))
            data = cursor.fetchall()
            self.title = data[0]
            self.content = data[1]
            self.updated_time = data[2]
            self.writer = data[3]
            conn.close()
        else:
            self.title = title
            self.content = content
    
    def get(id):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute(SELECT_POST_QUERY % (id))
        data = list(cursor.fetchall()[0])
        conn.close()
        return {'title': data[0], 'content' : data[1], 'updated_time': data[2], 'writer': data[3]}
