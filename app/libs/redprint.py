# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 15:06


# 红图 类似蓝图 用于注册路由
class Redprint(object):
    def __init__(self, name):
        self.name = name
        self.mound = []     # 保存注册路由集合

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, blue_print, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            # endpoint url_for()时传入使用
            endpoint = self.name + "+" + options.pop("endpoint", f.__name__)
            blue_print.add_url_rule(url_prefix + rule, endpoint, f, **options)




