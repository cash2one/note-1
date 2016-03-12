#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: worker.py
# Created: 18/12/2013 17:07:15
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

import threading


class Worker(Threading.Thread):
    requestID = 0

    def __init__(self, requestsQueue, resultQueue, **kwds):
        Threading.Thread.__init__(self, **kwds)
        self.setDaemon(1)
        self.workRequestQueue = requestsQueue
        self.resultQueue = resultsQueue
        self.start()

    def performWork(self, callable, *args, **kwds):
        """called by the main thread as callable would be, but w/o return"""
        Worker.requestID +=1
        self.workRequestQueue.put((Worker.requestID, callable, args, kwds))
        return Worker.requestID

    def run(self):
        while True:
            requestID, callable, args, kwds = self.workRequestQueue.get()
            self.resultQueue.put((requestID, callable(*args, **kwds)))


if __name__ == "__main__":
    pass

