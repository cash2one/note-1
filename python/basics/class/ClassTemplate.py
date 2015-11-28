# -*- coding: utf-8 -*-


class ClassName(Parent):

    """class documentation string"""

    # ---class_suite---

    # static variable

    def __init__(self, parent):
        # 初始化父类--super:获取父类引用
        super(ClassName, self).__init__(parent)

        # instance variable

        # init_suite

    def methodName(self):

        # method_suite

    def __privateMethodName(self):

        # method_suite

    def __del__(self):
        '一般不使用此方法--此方法只有在引用计数为0时才执行'
        Parent.__del__(self)

##############################################################################        
"静态方法与类方法"
##############################################################################

    @staticmethod
    def staticMethod():

        # method_suite

    def staticMethod():

        # method_suite
        # 使用模块函数比使用静态方法更常见

    staticMethod = staticmethod(staticMethod)


    @classmethod
    def classMethod(cls):

        # method_suite

    def classMethod(cls):

        # method_suite

    classMethod = classmethod(classMethod)


##############################################################################
'特殊的类属性'
##############################################################################  
Class.__name__ : 类的名字

Class.__doc__ : 类文档

Class.__bases__ : 所有父类,返回一个元组

Class.__dict__ : 类的属性,返回一个字典

Class.__module__ : 类定义所在的模块

Class.__class__ : 实例所对应的类

Class.__mro__ : MRO顺序

##############################################################################
'覆盖方法--重载'
##############################################################################
class Parent(object):
    def foo(self):
        #suite

class Sub(Parent):
    def foo(self):
        '父类的foo被覆盖了'

#被覆盖的基类方法还是可以被调用的
        Parent.foo(SubInstance)
        #更好的方法是:
        super(Sub,self).foo()

##############################################################################
'类，实例和其他对象的内建函数'
##############################################################################
issubclass(sub, parent)----判断sub是不是parent的子类，如果是返回True

python2.3之后parent可以是一个tuple, 如果sub是tuple中任一个类的子类就返回True
#
#
isinstance(obj1, obj2)----如果obj1是obj2的一个实例或其子类的一个实例, 就返回True
obj2一是可以用一个tuple的
#
#
#attr()系列函数可以在各种对象下工作,不限于类和实例
hasattr(obj, 'propertyname')----确定对象obj是否有一个特定的属性propertyname

getattr(obj, 'propertyname')----返回对象obj的属性propertyname的值

setattr(obj, 'propertyname', 'value')----设置属性值

delattr(obj, 'propertyname')----删除属性

#dir()
dir(object)----列出一个对象的所有属性
dir(module)----列出一个模块的所有属性

#vars()
vars()----与dir()相似,只是给定对象都必须有一个__dict__属性,返回一个属性和值的字典


#########################################################################
'用来定制类的特殊方法,可以模拟标准类型,重载操作符'
#########################################################################
#P391
__getattr__(self, name)  # 当特性name被访问且对象没有相应特性时被自动调用
__setattr__(self, name, value)  # 当试图给特性name赋值时被自动调用
__delattr__(self, name)  # 当试图删除特性name时被自动调用


# __getattr__实例
class Test(object):
    """
    __getattr__仅当属性不能在实例的__dict__或它的类(类的__dict__)或祖先类(其__dict__)中找到时才被调用
    """
    def __init__(self,name):
        self.name = name

    def __getattr__(self, value):
        if value == 'address':
            return 'China'

test = Test('letian')
print test.name
print test.address
test.address = 'Anhui'
print test.address


class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError



#########################################################################
'迭代器'
#########################################################################
#P399



#########################################################################
'私有化'
#########################################################################
"__" 类私有属性

"_" 单下划线用于模块私有属性，以防止" form name import* "的导入


#########################################################################
'新式类的高级特性'
#########################################################################
#__slots__
__slots__----是一个类变量，由一个序列对象组成，表示所有合法的实例属性，可以是一个
列表，元组或可迭代对象，如果要创建其名字不在__slots__中的实例属性将导致AttributeError


__getattribute__(self. name)  # 当特性name被访问时自动调用(只能在新式类中使用)


class Test(object):
    def __init__(self,name):
        self.name = name
    def __getattribute__(self, value):
        if value == 'address':
            return 'China'

test = Test('letian')
print test.name
print test.address
test.address = 'Anhui'
print test.addres


#########################################################################
'描述符'
#########################################################################
'''
描述符就是一个表示属性值的对象, 通过实现一个或多个特殊的__get__(), __set__(), __delete__()方法,
可以将描述符和属性机制挂钩, 还可以自定义这些操作
'''
#########################################################################






#########################################################################
'元类和__Metaclass__'
#########################################################################







#########################################################################
'抽象基类'
#########################################################################
from abc import ABCMeta, abstractmethod, abstractproperty

class Foo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def spam(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass


#########################################################################
'类装饰器'
#########################################################################
