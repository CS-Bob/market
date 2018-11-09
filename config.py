# encoding: utf-8
'''
@author: bo

@file: config.py
@time: 2018/10/31/031 20:23
@desc:
'''
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa_demo'
USERNAME = 'root'
PASSWORD = 'root'

# DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf-8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# DB_URI = 'mysql+pymysql://root:dzd123@localhost/zlktqa_demo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dzd123@localhost/你的数据库名'


DB_URI = 'postgresql://postgres:liuyubo110@127.0.0.1:5432/markets'
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
