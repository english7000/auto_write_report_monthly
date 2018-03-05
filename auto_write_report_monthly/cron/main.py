#coding=utf-8
#！/usr/bin/env python3



import paramiko
import docx


class ssh_conn(object):

    def __init_subclass__(self, host, port, username, passwd):
        self.host = host
        self.port = port
        self.username = username
        self.passwd = passwd
        self.ssh = None


    def conn(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh.connect(hostname=self.host, port= self.port, username=self.username, password=self.passwd)


    def get_data(self,command):
        stdin,stdout,stderr = self.ssh.exec_command(command)
        temp = stdout.read()
        res = temp if temp else stdout.read()
        return res


class report(object):


    def __init__(self,data):
            pass

    def draw_table(self):


