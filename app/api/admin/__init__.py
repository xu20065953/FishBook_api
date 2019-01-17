# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 15:36

from flask import Blueprint

from app.api.admin import user
from app.api.admin import client


def register_blueprint_admin():
    blue_print_admin = Blueprint("admin", __name__)

    user.api.register(blue_print_admin, url_prefix="/user")
    client.api.register(blue_print_admin, url_prefix="/client")

    return blue_print_admin

