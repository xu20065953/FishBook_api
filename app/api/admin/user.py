# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 15:37

from flask import jsonify

from app.libs.redprint import Redprint

api = Redprint("user")


@api.route("/get_admin", methods=["GET", "POST"])
def get_admin():
    return "get super user!"


