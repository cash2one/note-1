#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
from gevent import monkey; monkey.patch_all()
from gevent.queue import Queue, Empty


class Actor(gevent.Greenlet):

    def __init__(self, name, interval):
        self.inbox = Queue()
        self.name = name
        self.interval = interval
        super(Actor, self).__init__()

    def shutdown(self):
        self.running = False

    def work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        self.running = True
        while self.running:
            self.work()
            gevent.sleep(self.interval)


class Actor2(gevent.Greenlet):

    def __init__(self, name, interval):
        self.inbox = Queue()
        self.running = True
        self.name = name
        self.interval = interval
        super(Actor2, self).__init__()

    def work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        while True:
            try:
                msg = self.inbox.get(block=True, timeout=self.interval)
                if msg == 'stop':
                    break
            except Empty:
                self.work()

    def shutdown(self):
        self.inbox.put('stop')


class Pinger(Actor2):
    def work(self):
        print(self.name)


class Ponger(Actor2):
    def work(self):
        print(self.name)


ping = Pinger('AAAAAAA', 1)
pong = Ponger('BBBBBBB', 1)

ping.start()
pong.start()

gevent.sleep(10)

ping.shutdown()
pong.shutdown()

gevent.joinall([ping, pong])
