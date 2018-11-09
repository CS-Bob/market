# encoding: utf-8
'''
@author: bo

@file: manage.py
@time: 2018/10/31/031 22:22
@desc:
'''
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from market import app
from exts import db
from model import User


manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app,db)

# 添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
