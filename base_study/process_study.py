import multiprocessing
import time
import threading
import multiprocessing


class MyThread(threading.Thread):

    def run(self):
        time.sleep(1)
        a = 1 + 1
        print(a)

    def test_2(self):
        time.sleep(1)
        b = 1 + 2
        print(b)


if __name__ == '__main__':
    pass
