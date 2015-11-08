#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''doc string'''

class Base(object):
    name = ''
    version = ''
    
    def __init__(self):
        pass


class Sub(Base):
    name = 'sub'

    def __init__(self, *args, **kwargs):
        self.version = '1.0'

