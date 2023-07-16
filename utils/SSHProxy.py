# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 20:11
# @Author  : 石鑫磊
# @Site    : 
# @File    : SSHProxy.py
# @Software: PyCharm 
# @Comment :

import paramiko


class SSHProxy:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def open(self):
        # private_key=paramiko.RSAKey.from_private_key(self.password)
        self.transport = paramiko.Transport(self.hostname, self.port)
        # self.transport.connect(username=self.username, pkey=private_key)
        self.transport.connect(username=self.username, password=self.password)

    def close(self):
        self.transport.close()

    def command(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def command_queen(self, cmd, q):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        while not stdout.channel.exit_status_ready():
            result = stdout.readline()
            q.put(result)
            print('result', result)
            if stdout.channel.exit_status_ready():
                a = stdout.readlines()
                print('a', a)
                break

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()

    def download(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(remote_path, local_path)
        sftp.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == "__main__":
    with SSHProxy('192.168.1.99', 22, 'root', 'root') as ssh:
        res = ssh.command('df')
        print(res.decode('utf-8'))
