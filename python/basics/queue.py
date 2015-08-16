#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: queue.py
# Created: 13/12/2013 15:40:53
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue != []:
            return self.queue.pop(0)
        else:
            return None

    def length(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def flush(self):
        self.queue = []

    def preview(self):
        return self.queue

    def enqueueAtOppositeEnd(self, item):
        self.queue.insert(0,item)
        

class Queue2(object):
    def __init__(self, size):
        self.queue = []
        self.queue = size
        
    def enqueue(self, item):
        if len(self.queue)>=self.size:
            del self.queue[0]
            self.queue.append(item)
        else:
            self.queue.append(item)

    def dequeue(self):
        if self.queue != []:
            return self.queue.pop(0)
        else:
            return None

    def length(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def full(self):
        return len(self.queue)==self.size

    def flush(self):
        self.queue = []

    def preview(self):
        return self.queue

    def enqueueAtOppositeEnd(self, item):
        self.queue.insert(0,item)
