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
        doc = docx.Document()
        table = doc.add_table(rows=1, cols=3, style='Table Grid')  # 创建带边框的表格
        hdr_cells = table.rows[0].cells  # 获取第0行所有所有单元格
        hdr_cells[0].text = 'Name'
        hdr_cells[1].text = 'Id'
        hdr_cells[2].text = 'Desc'

        # 添加三行数据
        data_lines = 3
        for i in range(data_lines):
            cells = table.add_row().cells
            cells[0].text = 'Name%s' % i
            cells[1].text = 'Id%s' % i
            cells[2].text = 'Desc%s' % i

        rows = 2
        cols = 4
        table = doc.add_table(rows=rows, cols=cols)
        val = 1
        for i in range(rows):
            cells = table.rows[i].cells
            for j in range(cols):
                cells[j].text = str(val * 10)
                val += 1

        doc.save('tmp.docx')

