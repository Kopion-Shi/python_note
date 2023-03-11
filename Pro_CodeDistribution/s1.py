# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 15:44
# @Author  : 石鑫磊
# @Site    : 
# @File    : s1.py
# @Software: PyCharm 
# @Comment :
import time

from lib.get_logging import GetLogger

_logger_root = GetLogger().rootLogging()
_logger_app = GetLogger().app01Logging()

import threading
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def fun1(i):
    _logger_root.debug('root{}'.format(i))


def fun2():
    while True:
        for i in range(20):
            t = threading.Thread(target=fun1, args=(i,))
            t.setDaemon(True)
            t.start()
            t.join()



def run():
    p = multiprocessing.Process(target=fun1, )
    p.start()
    time.sleep(1)
    p.join()


if __name__ == "__main__":
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(fun2, i)
    pool.shutdown(True)
