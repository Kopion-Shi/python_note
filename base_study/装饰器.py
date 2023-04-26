# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 22:51
# @Author  : 石鑫磊
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm 
# @Comment :
import time


def log(func):
    def wrapper(*args, **kw):

        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def time_statistic(func):
    def wrapper(*args, **kw):
        start_time=time.time()
        func()
        print('运行时间：',time.time()-start_time)
        return func(*args, **kw)

    return wrapper

# @time_statistic
@log
def now():
    print ('2016-12-04')
    time.sleep(1)
if  __name__=="__main__":
    now()
