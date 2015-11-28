# -*- coding: utf-8 -*-

'''Functional Programming----函数式编程'''


# map
def func(x):
    return x*x

lst = range(10)

print map(func, lst)

print map(str, lst)

#--------------------------------------------------------------------------------
# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3...]上, 这个函数必须接收两个参数,
# 然后把结果继续和序列的下一个元素做累积计算
#--------------------------------------------------------------------------------
def add(x, y):
    return x+y

print reduce(add, [1,3,5,7,9])

def fn(x, y):
    return x*10 + y

print reduce(fn, [1,3,5,7,9])



def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int('13567')
# lambda函数进一步简化成
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))


#-----------------------------------------------------------------------------
# filter() 用于过滤序列
# 和map()类似, filter()也接收一个函数和一个序列, 不同的时, filter()把传入的函数依次作用于每个元素,
# 然后根据返回值是True还是False决定保留还是丢弃该元素.
#-----------------------------------------------------------------------------

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n%2 == 1

print filter(is_odd, [1,2,3,4,5,6,7,8,9])


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'b', None, 'c', '  ', 'ff'])


#-----------------------------------------------------------------------------
# sorted
# sorted()函数就是对list进行排序
#-----------------------------------------------------------------------------

# 升序排序
print sorted([36, 5, 12, 1, 9, 100, 9])


# 倒序排序
def reversed_cmp(x, y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print sorted([36, 5, 12, 1, 9, 100, 9], reversed_cmp)


# 字符串排序
print sorted(['bob', 'about', 'Zoo', 'Credit'])


# 忽略大小写的排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)



#-----------------------------------------------------------------------------
# 函数作为返回值
#-----------------------------------------------------------------------------

# 通常的求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
f
print f()

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”

# 注意一点，即使传入相同的参数, 当我们调用lazy_sum()时，每次调用都会返回一个新的函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1==f2


#-----------------------------------------------------------------------------
# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
#-----------------------------------------------------------------------------
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是： 都是9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
print f1()
print f2()
print f3()


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()


#-----------------------------------------------------------------------------
# 匿名函数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
#-----------------------------------------------------------------------------
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

f = lambda x: x * x
print f(5)

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数


#-----------------------------------------------------------------------------
# 偏函数
# functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#-----------------------------------------------------------------------------
print u'偏函数'

print int('12345')
print int('12345', base=8)
print int('12345', 16)

# 假设要转换大量的二进制字符串，每次都传入 int(x, base=2) 非常麻烦
# 于是，我们想到，可以定义一个 int2() 的函数，默认把 base=2 传进去
def int2(x, base=2):
    return int(x, base)

print int2('1000000')


# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
import functools

int2 = functools.partial(int, base=2)

print int2('1000000')

# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住(也就是设置默认值),
# 返回一个新的函数，调用这个新函数会更简单。
