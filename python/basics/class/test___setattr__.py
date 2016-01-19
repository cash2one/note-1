# -*- coding: utf-8 -*-

"""测试__setattr__ 和 __getattr__"""


class Book(object):

    def __init__(self, author, pub):
        self.author = author
        self.pub = pub
        self.extra_fields = {'one': 'one_value', 'two': 'two_value'}
    
    def __getattr__(self, item):
        print 'Nothing'
        try:
            return self.extra_fields[item]
        except KeyError:
            raise AttributeError        

    # 下面的方法会造成无限循环
    # def __setattr__(self, key, value):
    #     if hasattr(self, key):
    #         self[key] = value
    #     else:
    #         self.extra_fields[key] = value


book = Book('baixue', 'br')

print book.author
print book.pub
print book.one
