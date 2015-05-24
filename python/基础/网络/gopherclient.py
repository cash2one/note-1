#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: gopherclient.py
# Created: 14/01/2014 11:15:39
# Author: baixue
# Purpose:
#------------------------------------------------------------------------------

import socket, sys

port = 70
host = sys.argv[1]#命令行参数
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.conect((host, port))

s.sendall(filename + "\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
