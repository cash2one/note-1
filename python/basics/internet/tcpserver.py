#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: tcpserver.py
# Created: 04/12/2013 16:39:39
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

from socket import*
from time import ctime

HOST=''
PORT=1234
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)#5指最多允许多少个客户端连接到服务器

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpSerSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()

tcpSerSock.close()
            