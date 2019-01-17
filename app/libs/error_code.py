# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/16 16:07

from app.libs.error import ApiException


class Success(ApiException):
    """成功"""
    code = 201
    msg = "ok"
    error_code = 1

    def __init__(self, data=None):
        if data:
            self.data = data
        super(Success, self).__init__()


class ServerError(ApiException):
    """服务器错误"""
    code = 500
    msg = "sorry, 服务器发生了一些未知错误"
    error_code = 999


class AuthFailed(ApiException):
    """未登录，需要登录"""
    code = 401
    msg = "未授权..."
    error_code = 1005


class NotFound(ApiException):
    """url等资源未找到"""
    code = 404
    msg = "the resource is not found ..."
    error_code = 1001


class Forbidden(ApiException):
    """权限不足"""
    code = 403
    msg = "没有访问权限..."
    error_code = 1004


class ParameterError(ApiException):
    code = 400
    msg = "参数错误"
    form_msg = None
    error_code = 1000

    def __init__(self, form_errors=None):
        if form_errors:
            s = ""
            for k, v in form_errors.items():
                if s:
                    s += "\n"
                s += k + ": " + "".join(v)
            self.form_msg = s

        super(ParameterError, self).__init__()






