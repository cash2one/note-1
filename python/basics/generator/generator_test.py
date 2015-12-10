cd #!/usr/bin/env python
# -*- coding: utf-8 -*-

'''生成器测试'''

__author__ = 'Pysaoke'


def generator():
    for r in range(10):
        print r
        if r%2 == 0:
            yield 'even'
        else:
            yield 'odd'

def gen2():
    for r in range(10):
        print r
    else:
        yield 'done'
    print 111111111111111
    yield 'break'


if __name__ == "__main__":
    for i in gen2():
        print i
