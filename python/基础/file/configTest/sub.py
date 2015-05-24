#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

print "go"

while True:
    get = raw_input()
    if get == "1":
        break
    config.a += 1
    config.b += 2
    config.c += 3
    print config.a
    print config.b
    print config.c
