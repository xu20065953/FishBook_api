# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 14:43

from flask import Flask
from app.api.admin import register_blueprint_admin


# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(blueprint=register_blueprint_admin(), url_prefix="/admin")


# 注册插件
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


# 创建应用方法
def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    register_blueprints(app)
    register_plugin(app)

    return app


