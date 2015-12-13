# -*- coding: utf-8 -*-

'''生成器测试'''


def generator():
    for r in range(10):
        print r
        if r%2 == 0:
            yield 'even'
        else:
            yield 'odd'


def gen2():
    print '------------------------'
    for r in range(10):
        yield 'done%s' % r
    yield 'break'

if __name__ == "__main__":
    c = 0
    for i in gen2():
        print i
