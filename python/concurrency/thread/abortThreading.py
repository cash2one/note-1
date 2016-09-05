# -*- coding: utf-8 -*-
import time
import threading


class Worker(threading.Thread):
    def __init__(self, name='MyThread'):
        super(Worker, self).__init__(name=name)
        self._stop_event = threading.Event()
        self._sleep_period = 1.0

    def run(self):
        print " --- %s: start ---" % self.getName()
        count = 0
        while not self._stop_event.isSet():
            count += 1
            print "loop %d" % count
            self._stop_event.wait(timeout=self._sleep_period)
        print " --- %s: end ---" % self.getName()

    def join(self, timeout=None):
        self._stop_event.set()
        super(Worker, self).join(timeout=timeout)


if __name__ == "__main__":
    t = Worker()
    t.start()
    time.sleep(5.0)
    t.join()
