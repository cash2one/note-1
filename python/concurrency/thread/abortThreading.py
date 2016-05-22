#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# File: abortThreading.py
# Created: 17/01/2014 13:38:55
# Author: baixue
# Purpose:
# ------------------------------------------------------------------------------
import time
import threading


class Worker(threading.Thread):
    def __init__(self, name='TestThread'):
        super(Worker, self).__init__(name=name)
        self._stop_event = threading.Event()
        self._sleep_period = 1.0

    def run(self):
        print " --- %s: start ---" % self.getName()
        count = 0
        while not self._stop_event.isSet():
            count += 1
            print "loop %d" % count
            self._stop_event.wait(self._sleep_period)
        print " --- %s: end ---" % self.getName()

    def join(self, timeout=None):
        self._stop_event.set()
        super(Worker, self).join(timeout)


if __name__ == "__main__":
    t = Worker()
    t.start()
    time.sleep(5.0)
    t.join()
