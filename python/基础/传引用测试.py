#!/usr/bin/env python
# -*- coding: utf-8 -*-

def define():
    a = int(10)
    b = float(20.0)
    print id(a)
    print id(b)
    return a, b

x, y = define()

print
print id(x)
print id(y)








if __name__ == "__main__":
    pass
