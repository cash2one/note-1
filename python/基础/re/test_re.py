#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''re test'''

__author__ = 'baixue'

import re

s = 'speed=210,angle=150'
m = re.findall(r'(\w*[0-9]+)\w*', s)
print m

s = '103.1234?\r\n'
m = re.findall(r'\-?\d+\.?\d+', s)
print m

pattern = re.compile(r'\-?\d+\.?\d+')
match = pattern.search('103.1234?\r\n')
if match:
    print match.group()
# filter()
