#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
import threading


class ExternalInterfacing(threading.Thread):
    def __init__(self, externalCallable, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.setDaemon(1)
        self.externalCallable = externalCallable
        self.workRequestQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.start()

    def request(self, *args, **kwargs):
        """called by other threads as externalCallable would be"""
        self.workRequestQueue.put((args, kwargs))
        return self.resultQueue.get()

    def run(self):
        while True:
            args, kwargs = self.workRequestQueue.get()
            self.resultQueue.put(self.externalCallable(*args, **kwargs))
