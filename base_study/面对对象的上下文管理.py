# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 21:44
# @Author  : 石鑫磊
# @Site    : 
# @File    : 面对对象的上下文管理.py
# @Software: PyCharm 
# @Comment :
class Context:

    def do_something(self):
        pass

    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    def __exit__(self, *argsm,**kwargs):
        pass

with Context() as ctx:
    ctx.do_something()