#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
from gevent import monkey; monkey.patch_all()
from gevent.queue import Queue as G_Queue, Empty as G_Empty
from gevent.event import AsyncResult, Event

import threading
import multiprocessing
from Queue import Queue, Empty


# threading.Timer

class ThreadWorker(threading.Thread):

    def __init__(self, interval, name=''):
        super(ThreadWorker, self).__init__(name=name)
        self.setDaemon(1)
        self._interval = interval
        self._finished = threading.Event()

    def _work(self):
        raise NotImplemented()

    def run(self):
        self._finished.wait(timeout=self._interval)
        while not self._finished.is_set():
            self._work()
            self._finished.wait(timeout=self._interval)

    def shutdown(self):
        self._finished.set()

    def join(self, timeout=None):
        self._finished.set()
        super(ThreadWorker, self).join(timeout=timeout)


class ProcessWorker(multiprocessing.Process):

    def __init__(self, interval, name=''):
        super(ProcessWorker, self).__init__(name=name)
        self.daemon = True
        self._interval = interval
        self._finished = multiprocessing.Event()

    def _work(self):
        raise NotImplemented()

    def run(self):
        self._finished.wait(timeout=self._interval)
        while not self._finished.is_set():
            self._work()
            self._finished.wait(timeout=self._interval)

    def shutdown(self):
        self._finished.set()

    def join(self, timeout=None):
        self._finished.set()
        super(ProcessWorker, self).join(timeout=timeout)


class GeventWorker(gevent.Greenlet):

    def __init__(self, interval, name=''):
        self.name = name
        self._interval = interval
        self.running = True
        super(GeventWorker, self).__init__()

    def shutdown(self):
        self.running = False

    def _work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        while self.running:
            self._work()
            gevent.sleep(self._interval)


class ThreadActor(threading.Thread):

    def __init__(self, interval, name=''):
        super(ThreadActor, self).__init__(name=name)
        self.setDaemon(1)
        self._inbox = Queue()
        self._interval = interval
        self._timeout = None

    def _work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def run(self):
        while True:
            try:
                msg = self._inbox.get(block=True, timeout=self._timeout)
                if msg == 'stop':
                    self._timeout = None
                elif msg == 'start':
                    self._timeout = self._interval
                elif msg == 'exit':
                    break
            except Empty:
                self._work()

    def start(self):
        self._inbox.put('start')
        return super(ThreadActor, self).start()

    def stop(self):
        self._inbox.put('stop')

    def shutdown(self):
        self._inbox.put('exit')


class ProcessActor(multiprocessing.Process):

    def __init__(self, interval, name=''):
        super(ProcessActor, self).__init__(name=name)
        self.daemon = True
        self._inbox = multiprocessing.Queue()
        self._interval = interval
        self._timeout = None

    def _work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def run(self):
        while True:
            try:
                msg = self._inbox.get(block=True, timeout=self._timeout)
                if msg == 'stop':
                    self._timeout = None
                elif msg == 'start':
                    self._timeout = self._interval
                elif msg == 'exit':
                    break
            except Empty:
                self._work()

    def start(self):
        self._inbox.put('start')
        return super(ProcessActor, self).start()

    def stop(self):
        self._inbox.put('stop')

    def shutdown(self):
        self._inbox.put('exit')


class GeventActor(gevent.Greenlet):

    def __init__(self, interval, name=''):
        super(GeventActor, self).__init__()
        self.inbox = G_Queue()  # AsyncResult
        self._interval = interval
        self._timeout = None
        self.name = name

    def _work(self):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        while True:
            try:
                msg = self.inbox.get(block=True, timeout=self._timeout)
                if msg == 'stop':
                    self._timeout = None
                elif msg == 'start':
                    self._timeout = self._interval
                elif msg == 'exit':
                    break
            except G_Empty:
                self._work()
            gevent.sleep(0)

    def start(self):
        self.inbox.put('start')
        return super(GeventActor, self).start()

    def stop(self):
        self.inbox.put('stop')

    def shutdown(self):
        self.inbox.put('exit')
