#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@property

@property装饰器就是负责把一个方法变成属性调用的

'''

__author__ = 'baixue'


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Student(object):

    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# 下面的Student类的birth是可读写属性，而age就是一个只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


#--------------------------------------------------------------------------------------------------
class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)


class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, size):
        self.width, self.height = size

    @size.deleter
    def size(self):
        raise TypeError("can't delete size!")