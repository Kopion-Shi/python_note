import multiprocessing
import time
import threading
import multiprocessing

import time

import multiprocessing
import multiprocessing.pool
import time

from concurrent.futures import ProcessPoolExecutor


class Process_test():
    def __int__(self):
        pass

    def task1(self):
        while True:
            print('main1')
            time.sleep(1)

    def task2(self):
        print('main2')
        self.process_pool([self.task3, self.task4])

    def task3(self):
        print('tmain2_1')
        time.sleep(3)

    def task4(self):
        print('tmain2_2')
        time.sleep(4)

    def process_pool(self, task_list):
        pool = ProcessPoolExecutor(4)
        for task in task_list:
            pool.submit(task, )
        pool.shutdown()

    def double_process(self):
        p = multiprocessing.Process(target=self.task1)
        p.daemon = True
        p.start()
        self.task2()

    def main(self):
        self.double_process()


if __name__ == "__main__":
    p1 = Process_test()
    p1.main()
