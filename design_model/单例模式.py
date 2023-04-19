# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 22:00
# @Author  : 石鑫磊
# @Site    : 
# @File    : 单例模式.py
# @Software: PyCharm 
# @Comment :
import threading
import time



class Singleton():
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):  #hasattr() 函数用于判断对象是否包含对应的属性。
            orig = super()
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...", data)
        self.lock.release()



class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run..." % i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()
