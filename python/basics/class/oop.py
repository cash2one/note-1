# -*- coding: utf-8 -*-

class Base(object):
    def __init__(self, a, b):
        super(Base, self).__init__()
        self.a = a
        self.b = b

    def show(self):
        print 'base'
        print self.a
        print self.b


class A(Base):
    def __init__(self, a , b):
        super(A, self).__init__(a,b)


class B(Base):
    def __init__(self, *args):
        super(B, self).__init__(*args)


if __name__ == "__main__":
    a = A(1, 2)
    a.show()
    print a.a
    print a.b
    b = B(1,2)
    b.show
    print b.a
    print b.b
