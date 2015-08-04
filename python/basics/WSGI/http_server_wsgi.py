#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''简单http-server'''

__author__ = 'baixue'


from wsgiref.simple_server import make_server
from app_hello import application


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application2)
print "Serving HTTP on port 8000..."

# 开始监听HTTP请求:
httpd.serve_forever()
