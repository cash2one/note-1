#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import threading


class ExternalInterfacing(threading.Thread):
    def __init__(self, externalCallable, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(1)
        self.externalCallable = externalCallable
        self.workRequestQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.start()

    def request(self, *args, **kwds):
        """called by other threads as externalCallable would be"""
        self.workRequestQueue.put((args, kwds))
        return self.resultQueue.get()

    def run(self):
        while True:
            args, kwds = self.workRequestQueue.get()
            self.resultQueue.put(self.externalCallable(*args, **kwds))
