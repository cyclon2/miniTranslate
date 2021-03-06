import json
from textblob import TextBlob, Word
from flask import Flask, render_template, request, session, jsonify, redirect
from flask_restful import Api
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
import asyncio
from bs4 import BeautifulSoup
from db.User import User, find_userid
from db.Post import PostApi, Post
import db.word as wordObj
from db.sentence import Sentence
from utils.dic_daum import search_rough_all, search_detail_all
from utils.word import *

app = Flask(__name__,static_url_path='/static')
api = Api(app)
app.config['SECRET_KEY'] = "ut4u--nj0ai_0$o4q)6h4rrvgw6_qo246juzrzj%yz4rv8cvs^"
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/api/auth_func", methods=['POST'])
@login_required
def auth_func():
    user = current_user
    json_res = {'ok': True, 'msg': 'auth_func(%s),user_id=%s' % (request.json, user.user_id)}
    return jsonify(json_res)

@app.route("/api/notauth_func", methods=['POST'])
def notauth_func():
    json_res = {'ok': True, 'msg': 'notauth_func(%s)' % request.json}
    return jsonify(json_res)


##########
#        #
# LOGIN  #
#        #
##########

@app.route('/login', methods=['POST'])
def login():
    user = User(user_id = request.form['user_id'], password=request.form['password'])
    if user.login():
        user.authenticated = True
        login_user(user, remember=True)
    else:
        return render_template("login.html", message = "Invalid user_id or password")
    return redirect("/")


@app.route('/login', methods=['GET'])
def login_page():
    return render_template("login.html")

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template("signup.html")

@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect("/login")

@login_manager.user_loader
def user_loader(user_id):
    user =  find_userid(user_id)
    return user

#############
#           #
# TRANSLATE #
#           #
#############

@app.route('/', methods=["GET"])
@login_required
def main():
    personal_ignore_words = {}
    return render_template("main.html", data={'ignore_words' : except_words, 'personal_ignore_words': personal_ignore_words })

@app.route('/todo', methods=["GET"])
@login_required
def todo():
    return render_template("todo.html")

@app.route('/statistics', methods=["GET"])
@login_required
def get_statistics():
    return render_template("statistics.html")

@app.route('/mypage', methods=["GET"])
@login_required
def mypage():
    works = current_user.get_works()
    words = works['words']
    sentences = works['sentences']
    return render_template("mypage.html", data={"sentences": sentences, "words": words})

@app.route('/api/translate')
@login_required
def translate():
    to = request.args.get('to', default="ko")
    from_lang = request.args.get('from', default="en")
    sentence = request.args.get('q', '')
    if len(sentence) == 0:
        return json.dumps({ "result" : "" }, ensure_ascii=False), 200
    try:
        translate_sentence = TextBlob(sentence).translate(to=to, from_lang=from_lang).string
    except Exception as e:
        translate_sentence = sentence
    return json.dumps({ "result" : translate_sentence }, ensure_ascii=False), 200

@app.route('/api/definition/ko')
@login_required
def get_definition_ko():
    sentence = request.args.get('q', '')
    if len(sentence) == 0:
        return json.dumps({ "result" : "" }, ensure_ascii=False), 200
    words = TextBlob(sentence).words
    lemmatized_words = list(set(filter(lambda x : except_check(x), TextBlob(sentence).words)))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    definition_words = loop.run_until_complete(search_rough_all(lemmatized_words))
    loop.close()
    return json.dumps({ "result" : {"definitions":definition_words} }, ensure_ascii=False), 200

@app.route('/api/definition/en')
@login_required
def get_definition_en():
    sentence = request.args.get('q', '')
    if len(sentence) == 0:
        return json.dumps({ "result" : "" }, ensure_ascii=False), 200
    words = TextBlob(sentence).words
    lemmatized_words = list(set(map(lemmatize, words)))
    definition_words = list(map(definition, lemmatized_words))
    return json.dumps({ "result" : [ {"lemmatized":lemmatized_words},{"definitions":definition_words}] }, ensure_ascii=False), 200


##########
#        #
#  POST  #
#        #
##########

@app.route('/post/<post_id>', methods=["GET"])
@login_required
def get_post(post_id):
    post = Post.get(post_id)
    return render_template("post/post.html", post=post)

@app.route('/post/list', methods=["GET"])
@login_required
def post_list():
    posts = current_user.get_posts()
    return render_template("post/list.html", data=posts)

@app.route('/post/write', methods=["GET"])
@login_required
def post_write():
    return render_template("post/write.html")

@app.route('/post/write/<post_id>', methods=["GET"])
@login_required
def post_edit():
    return render_template("post/edit.html")


api.add_resource(Sentence, '/api/sentence', '/api/sentence/<int:sentenceid>')
api.add_resource(wordObj.Word, '/api/word')
api.add_resource(wordObj.Word2, '/api/words')

api.add_resource(PostApi, '/api/post')

if __name__ == '__main__':
    app.run("0.0.0.0", port=8000, debug=True)
