#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***************************************************************************
# File: stack.py
# Created: 17/12/2013 08:57:26
# Author: baixue
# Purpose:
# ***************************************************************************


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop(-1)

    def top(self):
        if self.items:
            return self.items[-1]

    def length(self):
        return len(self.items)

    def is_empty(self):
        return self.length() == 0
