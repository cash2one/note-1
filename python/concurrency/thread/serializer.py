#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import threading


class Serializer(threading.Thread):
    def __init__(self, **kwds):
        super(Serializer, self).__init__(self, **kwds)
        # 设置为"守护线程", 主线程退出时, 不用等待它结束
        self.setDaemon(1)
        self.workRequestQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.start()

    def apply(self, callable, *args, **kwargs):
        """called by other threads callable would be"""
        self.workRequestQueue.put((callable, args, kwargs))
        return self.resultQueue.get()

    def run(self):
        while True:
            callable, args, kwds = self.workRequestQueue.get()
            self.resultQueue.put(callable(*args, **kwds))
