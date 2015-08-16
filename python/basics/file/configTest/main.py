#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import function


print config.a
print config.b
print config.c


while True:
    function.add()
    get = raw_input()
    print config.a
    print config.b
    print config.c
    
    if config.c==12:
        break



if __name__ == '__main__':
    pass
