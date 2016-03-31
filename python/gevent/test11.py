#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
猴子补丁(Monkey patching)
monkey.patch_socket()这个命令，这个纯粹副作用命令是用来改变标准socket库的.
gevent能够 修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行.
"""


import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
