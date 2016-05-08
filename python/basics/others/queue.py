#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **********************************************************************
# File: queue.py
# Created: 13/12/2013 15:40:53
# Author: baixue
# Description:
# **********************************************************************


class Queue(object):
    def __init__(self, size):
        self.items = []
        self.size = size

    def enqueue(self, item):
        if len(self.items) >= self.size:
            del self.items[0]
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def length(self):
        return len(self.items)

    def is_empty(self):
        return self.length() == 0

    def full(self):
        return self.length() == self.size

    def flush(self):
        self.items = []

    def preview(self):
        return self.items

    def enqueue_at_opposite_end(self, item):
        self.items.insert(0, item)
