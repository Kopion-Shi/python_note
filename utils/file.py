# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 16:38
# @Author  : 石鑫磊
# @Site    : 
# @File    : file.py
# @Software: PyCharm 
# @Comment :
class File:
    def __init__(self,path):
        self.path=path
    def read_file(self):
        with open(self.path,mode='a',encoding='utf-8')as f:
            content=f.read()
        return content
