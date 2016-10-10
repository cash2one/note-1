#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from SocketServer import ThreadingTCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def setup(self):
        StreamRequestHandler.setup(self)
        self.remote_addr = self.request.getpeername()
        print '%s:%s connected...' % self.remote_addr, time.ctime()

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if data:
                self.request.send('[%s] %s' % (time.ctime(), data))
            else:
                # 客户端关闭连接后, 会收到一个空字符串
                break

    def finish(self):
        StreamRequestHandler.finish(self)
        print '%s:%s done' % self.remote_addr, time.ctime()


if __name__ == "__main__":
    server = ThreadingTCPServer(('', 5555), Handler)
    server.serve_forever()
