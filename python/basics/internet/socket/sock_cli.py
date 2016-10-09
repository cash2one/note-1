#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import socket


HOST = 'localhost'
PORT = 5555


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))


sock.send('msg-1')
data = sock.recv(1024)
print data

sock.send('msg-2')
data = sock.recv(1024)
print data

for _ in range(10):
    print 'waiting...'
    time.sleep(1)

sock.close()   # 关闭连接
