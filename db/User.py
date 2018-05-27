import pymysql
from db.setting import *
from db.Query import *

class User:
    def __init__(self, user_id, email=None, password=None,
                 authenticated=False):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.authenticated = authenticated

    def __repr__(self):
        r = {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'authenticated': self.authenticated,
        }
        return str(r)

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    
    def login(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        sql = "SELECT EXISTS( SELECT * FROM `User` WHERE `userid` = %s and `password` = %s)";
        cursor.execute(sql, (self.user_id, self.password))
        is_found = cursor.fetchall()[0][0]
        conn.close()
        return is_found == 1
    
    def signup(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        sql = "INSERT INTO `User` (`userid`, `password`, `email`) VALUES(%s, %s, %s);"
        cursor.execute(sql, (self.user_id, self.password, self.email))
        conn.commit()
        conn.close()
    
    def get_works(self):
        conn = pymysql.connect(host=DB_HOST, 
            user=DB_USER, password=DB_PASSWORD,
            db='toy', charset='utf8'
        )
        cursor = conn.cursor()
        info = dict({})
        cursor.execute(USERWORD_LIKE_QUERY % (self.user_id))
        info['words'] = list(cursor.fetchall())
        cursor.execute(SENTENCE_QUERY % (self.user_id))
        info['sentences'] = list(cursor.fetchall())
        conn.close()
        return  info   

def find_userid(user_id):
    conn = pymysql.connect(host=DB_HOST, 
        user=DB_USER, password=DB_PASSWORD,
        db='toy', charset='utf8'
    )
    cursor = conn.cursor()
    sql = "SELECT * FROM `User` WHERE `userid` = %s";
    cursor.execute(sql, (user_id))
    user =  cursor.fetchall()
    if len(user) == 0:
        conn.close()
        return User('no-one')
    user = user[0]
    conn.close()
    return User(user_id=user[1], email=user[3])

if __name__ == '__main__':
    User('admin').get_info()
    