# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 16:32

from flask import request, json
from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    code = 500
    msg = "sorry we made a mistake!"      # 提示信息
    form_msg = None     # 表单验证返回的错误信息
    data = None     # 返回的数据
    error_code = 999    # 未知错误

    def __init__(self, msg=None, data=None, code=None, error_code=None, form_msg=None, headers=None):
        if msg:
            self.msg = msg
        if data:
            self.data = data
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if form_msg:
            self.form_msg = form_msg

        super(ApiException, self).__init__(msg, None)

    # 重写get_body方法
    def get_body(self, environ=None):
        """返回json"""
        body = dict(
            msg=self.msg,
            form_msg=self.form_msg,
            error_code=self.error_code,
            data=self.data,
            request=request.method + " " + self.get_url_no_param()
        )
        # print(body)
        return json.dumps(body)

    # 重写get_headers方法
    def get_headers(self, environ=None):
        """返回json header"""
        return [("Content-Type", "application/json")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]






