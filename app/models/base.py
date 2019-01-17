# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 17:53

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, DateTime, SmallInteger
from contextlib import contextmanager

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if "status" not in kwargs.keys():
            kwargs["status"] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(DateTime, default=datetime.now)
    status = Column(SmallInteger, default=1)    # 1：表示正常 0：表示删除（软删除）

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) != "id":
                setattr(self, key, value)

    # 删除方法
    def delete(self):
        self.status = 0

    # 需要被序列化的字段
    def keys(self):
        return self.fields

    # 隐藏某个序列化的字段
    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    # 添加某个需要被序列化的字段
    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self



