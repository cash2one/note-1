#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Python 中的 is 和 id'''


#----------------(ob1 is ob2) 等价于 (id(ob1) == id(ob2))------------------#
'''
首先id函数可以获得对象的内存地址，如果两个对象的内存地址是一样的，那么这两个对象肯定是一个对象。和is是等价的。Python源代码为证。
'''
static PyObject *
    cmp_outcome(int op, register PyObject *v, register PyObject *w)
{
    int res = 0;
    switch (op) {
    case PyCmp_IS:
    res = (v == w);
    break;
    case PyCmp_IS_NOT:
    res = (v != w);
    break;

'''
但是请看下边代码的这种情况怎么会出现呢？
'''
def bar(self, x):
    return self.x + y

class Foo(object):
    x = 9
    def __init__(self ,x):
        self.x = x
    bar = bar

foo = Foo(5)
foo.bar is Foo.bar  # False
id(foo.bar) == id(Foo.bar)  # True

'''
两个对象用is判断是False，用id判断却是True，这与我们已知的事实不符啊.
这种现象该如何解释呢？遇到这种情况最好的解决方法就是调用dis模块去看下两个比较语句到底做了什么。
'''
import dis

dis.dis("id(foo.bar) == id(Foo.bar)")

dis.dis("foo.bar is Foo.bar")

'''
真实情况是当执行.操作符的时候，实际是生成了一个proxy对象,
foo.bar is Foo.bar的时候,
两个对象顺序生成，放在栈里相比较，由于地址不同肯定是False.
但是id(foo.bar) == id(Foo.bar)的时候就不同了，
首先生成foo.bar,然后计算foo.bar的地址，计算完之后foo.bar的地址之后，就没有任何对象指向foo.bar了
所以foo.bar对象就会被释放。然后生成Foo.bar对象，
由于foo.bar和Foo.bar所占用的内存大小是一样的,
所以又恰好重用了原先foo.bar的内存地址，所以id(foo.bar) == id(Foo.bar)的结果是True。
'''

'''
用id(expression a) == id(expression b)来判断两个表达式的结果是不是同一个对象的想法是有问题的。

foo.bar 这种形式叫 attribute reference [1]，它是表达式的一种。
foo是一个instance object,bar是一个方法，这个时候表达式foo.bar返回的结果叫method object [2]。
foo.bar本身并不是简单的名字，而是表达式的计算结果，是一个 method object，在id(foo.bar)这样的表达式里，
method object只是一个临时的中间变量而已，对临时的中间变量做id是没有意义的。
一个更明显的例子是，
'''
print id(foo.bar) == id(foo.__init__)  # True

'''
只有你能保证对象不会被销毁的前提下，你才能用 id 来比较两个对象。所以，如果你非要比的话，得这样写：
'''
fb = foo.bar
Fb = Foo.bar
print id(fb) == id(Fb)

'''
即把两个表达式的结果绑定到名字上，再来比是不是同一个对象，你才能得到正确的结果。
'''

'''
is表达式 [4] 也是一样的，你现在得到了正确的结果，完全是因为 CPython 现在的实现细节决定的。
现在的is的实现，是左右两边的对象都计算出来，然后再比较这两个对象的地址是否一样。
万一哪天改成了，先算左边，保存地址，把左边释放掉，再算右边，再比较的话，你的is的结果可能就错了。
官方文档里也提到了这个问题 [5]。
我认为正确的方法也是像id那样，先把左右两边都计算下来，并显式绑定到各自的名字上，然后再用is判断。
'''























