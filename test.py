# encoding: utf-8
'''
@author: bo

@file: test.py
@time: 2018/11/8/008 19:11
@desc:
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('regist_code.html')


if __name__ == '__main__':
    app.run()
