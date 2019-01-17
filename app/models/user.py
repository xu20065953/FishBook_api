# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/17 9:51

from sqlalchemy import Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=True)
    nickname = Column(String(24))
    age = Column(SmallInteger)
    auth = Column(SmallInteger, default=1)
    _password = Column("password", String(124))

    @orm.reconstructor
    def __init__(self):
        self.field = ["id", "email", "nickname", "auth", "age"]

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 邮箱注册
    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)






