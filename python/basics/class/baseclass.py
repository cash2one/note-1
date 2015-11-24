# -*- coding: utf-8 -*-

""" test """


class Base(object):
    pass


setattr(Base, 'name', 'baseclass')
setattr(Base, 'version', 1.0)

print dir(Base)

