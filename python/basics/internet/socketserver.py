#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: socketserver.py
# Created: 23/01/2014 10:41:27
# Author: baixue
# Purpose:
#------------------------------------------------------------------------------

from SocketServer import ThreadingTCPServer, ThreadingMixIn, StreamRequestHandler
from time import ctime


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr, ctime()
        while True:
            data = self.request.recv(1024)
            if len(data)==0:
                #如果客户端断开连接,data==0
                print "done"
                break
            else:
                self.request.write('Server get %s at:%s'%(data.upper(),ctime()))
                #self.wfile是将数据写入客户端的类文件对象
                #self.rfile是从客户端读取数据的类文件对象
            


if __name__ == "__main__":
    server = ThreadingTCPServer(('', 1234), Handler)
    server.serve_forever()
