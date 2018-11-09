# encoding: utf-8
'''
@author: bo

@file: model.py
@time: 2018/10/31/031 20:42
@desc:
'''
from datetime import datetime

from exts import db
u"""
        字段	类型	空	默认	注释
        id	int(10)	否		自增ID
        user_name	varchar(50)	否		用户名
        password	varchar(255)	否		密码
        avatar	varchar(255)	否		头像
        email	varchar(20)	是		邮箱号码
        is_student	tinyint(3)	否	0	是否学生身份，1为是，0为否
        student_name	varchar(255)	是		学生用户真实姓名
        remember_token	varchar(100)	是		
        status	tinyint(3)	否	1	状态，0为禁用，1为正常
        deleted_at	tinyint(3)	否	1	软删除字段,0为已删除，1为未删除
        created_time	datetime	否		注册时间
        updated_time	datetime	否		更新时间
    """

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    avatar = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(20),nullable=True)
    is_student = db.Column(db.Boolean,nullable=False)
    student_name = db.Column(db.String(255),nullable=True)
    remember_token = db.Column(db.String(100),nullable=True)
    status = db.Column(db.Boolean,nullable=False)
    deleted_at = db.Column(db.Boolean,nullable=False)
    created_time = db.Column(db.DateTime,nullable=False,default=datetime.now())
    updated_time = db.Column(db.DateTime,nullable=False,default=datetime.now())


