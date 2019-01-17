# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/17 10:52

from flask import request
from flask_wtf import FlaskForm
from app.libs.error_code import ParameterError


class BaseForm(FlaskForm):
    def __init__(self):
        super(BaseForm, self).__init__(data=request.json)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate_on_submit()
        if not valid:
            raise ParameterError(self.errors)

        return self



