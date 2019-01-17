# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/01/14 14:42

# jsonify 返回数据支持中文
JSON_AS_ASCII = False


# mysql
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:1234+abcd@localhost:3306/fish_book"
# sql server
# SQLALCHEMY_DATABASE_URI = "mssql+pymssql://username:passwordc@localhost:1433/database"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# SECRET_KEY 生成方法
# import os
# os.urandom(24)
SECRET_KEY = '\xae\xaaX\x08\xe4w\xfec#F\xcc\x15k\xa7\x80"qd\x8a\x8b\x13\xfdM7'

# token 过期时间
TOKEN_EXPIRATION = 24 * 3600

# 取消 flask csrf 保护
WTF_CSRF_ENABLED = False



