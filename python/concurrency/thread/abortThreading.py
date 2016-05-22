#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# File: abortThreading.py
# Created: 17/01/2014 13:38:55
# Author: baixue
# Purpose:
# ------------------------------------------------------------------------------

import threading


class TestThread(threading.Thread):
    def __init__(self, name='TestThread'):
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)

    def run(self):
        # 主循环
        print "%s starts" % self.getName()
        count = 0
        while not self._stopevent.isSet():
            count += 1
            print "loop %d" % count
            self._stopevent.wait(self._sleepperiod)
        print "%s ends" % self.getName()

    def join(self, timeout=None):
        # 终止线程并等待结束
        self._stopevent.set()
        threading.Thread.join(self, timeout)


if __name__ == "__main__":
    testthread = TestThread()
    testthread.start()
    import time
    time.sleep(5.0)
    testthread.join()      
