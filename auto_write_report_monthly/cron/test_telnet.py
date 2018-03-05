#coding=utf-8
#！/usr/bin/env python3

import  telnetlib
import io



finish = b'>'
tn = telnetlib.Telnet('172.17.6.251','23')
tn.read_until(b'Username:')
tn.write(b'admin\n')
tn.read_until(b'Password:')
tn.write(b'1Lbccszh\n')
tn.read_until(finish)

tn.write(b'show ver\n')
# res =tn.read_until('alarm '.encode('utf-8'))

res = tn.read_until(finish,timeout=2)

if b'--More--' in res:              #由于命令会出现翻页所以用循环来收取结果
    res_add = b''
    while finish.decode() not in res_add.decode():
        tn.write(b'\n')
        res_add= tn.read_until(finish,timeout=2)
        res += res_add


res = res.decode()
buf = io.StringIO(res)          #使用io.StringIO来一行一行输出res
print(buf.readline())


tn.close()# tn.write('exit\n')