from multiprocessing import Process, Queue, set_start_method
from utils.SSHProxy import SSHProxy

q1 = Queue()


def q_check(exp):
    while True:
        res = q1.get()
        if res:
            print(f'q_check running{res}')
            if exp in str(res):
                print('预期结果get')
class Myprocess():

    def __int__(self):
        pass

    def sub_process(self, task_list, ):
        sub_task_list = []
        for task in task_list:
            c1 = Process(target=task, )
            sub_task_list.append(c1)
            # 开始
        for sub_task in sub_task_list:
            sub_task.daemon = True
            sub_task.start()
        for sub_task in sub_task_list:
            sub_task.join()


class Process_message():
    def __int__(self):
        pass

    def cmd_run(self, cmd):
        with SSHProxy('192.168.80.4', 22, 'sxl', 'sxl') as ssh:
            print('product running')
            ssh.command_queen(cmd, q1)


    def upload(self):
        with SSHProxy('192.168.80.4', 22, 'sxl', 'sxl') as ssh:
            ssh.upload('./test.sh', './test.sh')


def sub1():
    p = Process_message()
    # p.upload()
    p.cmd_run(cmd='./test.sh', )


def sub2():
    q_check('10')


if __name__ == '__main__':
    m = Myprocess()
    sub_list = [sub1, sub2]
    m.sub_process(sub_list, )
