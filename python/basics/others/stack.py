#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: stack.py
# Created: 17/12/2013 08:57:26
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.apend(item)

    def pop(self):
        if self.stack!=[]:
            return self.stack.pop(-1)
        else:
            return None

    def top(self):
        if self.stack!=[]:
            return self.stack[-1]
        else:
            return None

    def length(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []
