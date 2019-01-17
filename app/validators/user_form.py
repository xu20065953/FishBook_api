# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/17 11:17

from wtforms import IntegerField, StringField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp

from app.models.user import User
from app.validators.base import BaseForm as Form


class UserEmailForm(Form):
    account = StringField(validators=[Email(message="请填写正确的邮箱！")])
    secret = StringField(validators=[
        DataRequired(message="您还没有填写密码！"),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message="密码应由6-22位数字，大小写字符或_*&$#@字符组成！")
    ])
    nickname = StringField(validators=[DataRequired(message="您还没有填写昵称!"), Length(min=2, max=22, message="昵称需要2-22位！")])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message="邮箱已注册")




