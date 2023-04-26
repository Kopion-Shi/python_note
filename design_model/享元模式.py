# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 18:34
# @Author  : 石鑫磊
# @Site    : 
# @File    : 享元模式.py
# @Software: PyCharm 
# @Comment :
import time

from concurrent.futures import ProcessPoolExecutor


def time_statistic(func):
    def wrapper(self, *args, **kw):
        start_time = time.time()
        func_ = func(self, *args, **kw)
        print('运行时间：', time.time() - start_time)
        return func_

    return wrapper


class Coffee:
    name = ''
    price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)

    def show(self):
        print('start make coffo')
        time.sleep(10)
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


class Customer:
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_factory(coffee_name)


class CoffeeFactory():
    coffee_dict = {}

    def getCoffee(self, name):
        if self.coffee_dict.has_key(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


class Run():
    def task(self, i):
        cu1 = Customer('sxl{}'.format(i), CoffeeFactory)
        cu1.order('香飘').show()

    @time_statistic
    def task_multilprocess(self):
        pool = ProcessPoolExecutor(16)
        for i in range(100):
            pool.submit(self.task, i)  ##done有mainProcess处理，线程池中由subthreading处理
        pool.shutdown(True)


if __name__ == "__main__":
    Run().task_multilprocess()

###享元模式定义如下：使用共享对象支持大量细粒度对象。
# 大量细粒度的对象的支持共享，可能会涉及这些对象的两类信息：内部状态信息和外部状态信息。
# 内部状态信息就是可共享出来的信息，它们存储在享元对象内部，不会随着特定环境的改变而改变；外部状态信息就不可共享的信息了
# 享元模式中只包含内部状态信息，而不应该包含外部状态信息。这点在设计业务架构时，应该有所考虑。

