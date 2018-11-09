# encoding: utf-8
'''
@author: bo

@file: decorators.py
@time: 2018/11/6/006 0:11
@desc:
'''

from functools import wraps
from flask import session,redirect,url_for

#登录限制
def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
