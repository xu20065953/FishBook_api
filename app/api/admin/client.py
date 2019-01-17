# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/17 10:23

from app.libs.redprint import Redprint
from app.validators.user_form import UserEmailForm


api = Redprint("client")


@api.route("/register", methods=["POST"])
def register():
    # 1/0
    form = UserEmailForm().validate_for_api()
    print(form)
    return "register"




