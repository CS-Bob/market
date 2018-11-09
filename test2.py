# encoding: utf-8
'''
@author: bo

@file: test2.py
@time: 2018/11/8/008 20:16
@desc:
'''
from flask import Flask, session, escape, request

app = Flask(__name__)
app.secret_key = 'please-generate-a-random-secret_key'


@app.route("/")
def index():

    if 'username' in session:
        return 'hello, {}\n'.format(escape(session['username']))
    return 'hello, stranger\n'


@app.route("/login", methods=['GET','POST'])
def login():
    session['username'] = '123'
    a = session.get('username')
    print(a)
    return 'login success'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
