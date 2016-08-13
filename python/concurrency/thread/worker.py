#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading


class Worker(threading.Thread):
    request_id = 0

    def __init__(self, req_q, res_q, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.setDaemon(1)
        self.requests_queue = req_q
        self.result_queue = res_q
        self.start()

    def perform_work(self, func, *args, **kwargs):
        """called by the main thread as callable would be, but w/o return"""
        Worker.request_id += 1
        self.requests_queue.put((Worker.request_id, func, args, kwargs))
        return Worker.request_id

    def run(self):
        while True:
            requestID, callable, args, kwds = self.requests_queue.get()
            self.result_queue.put((requestID, callable(*args, **kwds)))


if __name__ == "__main__":
    pass
