#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''技巧'''

__author__ = 'baixue'


# 用可迭代对象创建列表
lst = ['a', 'b', 'c', 'd']
iterobj = enumerate(lst)
lista = list(iterobj)

# 用可迭代对象的前N个元素创建list
import itertools
y = list(itertools.islice(lst, N))

# 并行地循环多个可迭代对象
a = ['a1', 'a2', 'a3', 'a4', 'a5']
b = ['b1', 'b2', 'b3']
import itertools
for x, y in itertools.izip(a, b):
    print x, y

# 内建函数zip是个备选方案，缺点是它可能会损害性能
for x, y in zip(a, b):
    print x, y

# 如果迭代多个不同长度的可迭代对象，最短的可迭代对象耗尽时，zip和itertools.izip都会停止
# 在较短的可迭代对象中填充None，直到和最长的相等
for x, y in map(None, a, b):
    print x, y

# 用None之外的值填充
# 如果只有两序列用这个函数
import itertools
def par_two(a, b, padding_item=None):
    a, b = iter(a), iter(b)
    # 首先，对两者用izip处理，直达其中一个耗尽
    for x in itertools.izip(a, b):
        yield x
    # 下面两个循环最多只有一个能够执行
    # 因为此时a或b至少有一个是耗尽的
    for x in a:
        yield x, padding_item
    for x in b:
        yield padding_item, x

# 通用的，任意数目的序列
def par_loop(padding_item, *sequences):
    iterators = map(iter, sequences)
    num_remaining = len(iterators)
    result = [padding_item] * num_remaining
    while num_remaining:
        for i, it in enumerate(iterators):
            try:
                result[i] = it.next()
            except StopIteration:
                iterators[i] = itertools.repeat(padding_item)
                num_remaining -= 1
                result[i] = padding_item
        if num_remaining:
            yield tuple(result)


def smallmerge(*sequences):
    '''合并有序序列'''
    result = []
    for subseq in sequences:result.extend(subseq)
    return result


#-------------------无需过多援引 ，创建字典---------------------#
dt = dict(zip(keys, values))
dt = dict(itertools.izip(keys, values))

dt = dict(map(None, a, range(3)))
import string
count_by_letter = dict.fromkeys(string.ascii_lowercase, 0)


#-------------------字典操作技巧---------------------#
import itertools

HEADER = ('name', 'id', 'cell', 'mail')

lines = [[i for x in range(4)] for i in range(10000)]
print len(lines)

def tansform_user_data(user_data):
    '''将列表构建成和字段对应的字典'''
##    line = ['' for i in range(len(HEADER))]
##    dict_data = dict(zip(HEADER, line))
    # 字典推导式
    # dict_data = { h:'' for h in HEADER }
    dict_data = dict.fromkeys(HEADER, '')
    dict_list = []
    for data in user_data:
        dt = dict_data.copy()
        for idx, field in enumerate(HEADER):
            dt[field] = data[idx]
        dict_list.append(dt)
    return dict_list


def tansform_user_data10(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_data = dict.fromkeys(HEADER, '')
    dict_list = []
    for data in user_data:
        dt = dict_data.copy()
        for h, d in itertools.izip(HEADER, data):
            dt[h] = d
        dict_list.append(dt)
    return dict_list


def tansform_user_data2(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_list = []
    for data in user_data:
        dt = dict(zip(HEADER, data))
        dict_list.append(dt)
    return dict_list


def tansform_user_data3(lines):
    '''将列表构建成和字段对应的字典'''
    return [dict(itertools.izip(HEADER, line)) for line in lines]


def tansform_user_data4(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_list = []
    for data in user_data:
        dt = dict({'id':'', 'name':''})
        for idx, field in enumerate(HEADER):
            dt[field] = data[idx]
        dict_list.append(dt)
    return dict_list



#-------------------拆箱---------------------#
a, b, c = 1, 2, 3
print a, b, c

a, b, c = [1, 2, 3]

a, b, c = (2 * i + 1 for i in range(3))

a, (b, c), d = [1, (2, 3), 4]


#-------------------拆箱变量交换---------------------#
a, b = 1, 2
a, b = b, a


#-------------------扩展拆箱（只兼容python3）---------------------#
a, *b, c = [1, 2, 3, 4, 5]


#-------------------负数索引---------------------#
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[-1]
a[-3]


#-------------------切割列表---------------------#
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[2:8]


# 指定步长切割列表
a[::2]  # [0, 2, 4, 6, 8, 10]
a[::3]  # [0, 3, 6, 9]
a[2:8:2]  # [2, 4, 6]


# 负数步长切割列表
a[::-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a[::-2]  # [10, 8, 6, 4, 2, 0]


# 列表切割赋值
a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print a  # [1, 2, 0, 0, 4, 5]
a[1:1] = [8, 9]
print a  # [1, 8, 9, 2, 0, 0, 4, 5]
a[1:-1] = []
print a  # [1, 5]


# 命名列表切割方式
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
LASTTHREE  # slice(-3, None, None)
a[LASTTHREE]  # [3, 4, 5]


# 列表以及迭代器的压缩和解压缩
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a, b)
print z  # [(1, 'a'), (2, 'b'), (3, 'c')]

zip(*z)  # [(1, 2, 3), ('a', 'b', 'c')]


# 列表相邻元素压缩器
a = [1, 2, 3, 4, 5, 6]
zip(*([iter(a)] * 2))  # [(1, 2), (3, 4), (5, 6)]

group_adjacent = lambda a, k: zip(*([iter(a)] * k))
group_adjacent(a, 3)  # [(1, 2, 3), (4, 5, 6)]
group_adjacent(a, 2)  # [(1, 2), (3, 4), (5, 6)]
group_adjacent(a, 1)  # [(1,), (2,), (3,), (4,), (5,), (6,)]

zip(a[::2], a[1::2])  # [(1, 2), (3, 4), (5, 6)]
zip(a[::3], a[1::3], a[2::3])  # [(1, 2, 3), (4, 5, 6)]

group_adjacent = lambda a, k: zip(*(a[i::k] for i in range(k)))
group_adjacent(a, 3)  # [(1, 2, 3), (4, 5, 6)]
group_adjacent(a, 2)  # [(1, 2), (3, 4), (5, 6)]
group_adjacent(a, 1)  # [(1,), (2,), (3,), (4,), (5,), (6,)]


# 在列表中用压缩器和迭代器滑动取值窗口
def n_grams(a, n):
    z = [iter(a[i:]) for i in range(n)]
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
n_grams(a, 3)  # [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
n_grams(a, 2)  # [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
n_grams(a, 4)  # [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]


# 用压缩器反转字典
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
m.items()  # [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
zip(m.values(), m.keys())  # [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
mi = dict(zip(m.values(), m.keys()))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# 列表展开
a = [[1, 2], [3, 4], [5, 6]]
list(itertools.chain.from_iterable(a))  # [1, 2, 3, 4, 5, 6]
sum(a, [])  # [1, 2, 3, 4, 5, 6]
[x for l in a for x in l]  # [1, 2, 3, 4, 5, 6]

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
[x for l1 in a for l2 in l1 for x in l2]  # [1, 2, 3, 4, 5, 6, 7, 8]

a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
flatten(a)  # [1, 2, 3, 4, 5, 6, 7, 8]


# 生成器表达式
g = (x ** 2 for x in xrange(10))
next(g)  # 0
next(g)  # 1
sum(x ** 3 for x in xrange(10))  # 2025
sum(x ** 3 for x in xrange(10) if x % 3 == 1)  # 408


# 字典推导
m = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

m = {x: 'A' + str(x) for x in range(10)}
# {0: 'A0', 1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9'}


# 用字典推导反转字典
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

{v: k for k, v in m.items()}
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# 命名元组
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
p  # Point(x=1.0, y=2.0)
p.x  # 1.0
p.y  # 2.0


# 继承命名元组
class Point(collections.namedtuple('PointBase', ['x', 'y'])):
    __slots__ = ()
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

p = Point(x=1.0, y=2.0)
q = Point(x=2.0, y=3.0)
p + q  # Point(x=3.0, y=5.0)


# 操作集合
A = {1, 2, 3, 3}
print A  # set([1, 2, 3])
B = {3, 4, 5, 6, 7}
print B  # set([3, 4, 5, 6, 7])

A | B  # set([1, 2, 3, 4, 5, 6, 7])

A & B  # set([3])

A - B  # set([1, 2])
B - A  # set([4, 5, 6, 7])

A ^ B  # set([1, 2, 4, 5, 6, 7])

(A ^ B) == ((A - B) | (B - A))  # True


# 操作多重集合
A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])
A  # Counter({2: 2, 1: 1})
B  # Counter({2: 2, 3: 1})

A | B  # Counter({2: 2, 1: 1, 3: 1})

A & B  # Counter({2: 2})

A + B  # Counter({2: 4, 1: 1, 3: 1})

A - B  # Counter({1: 1})
B - A  # Counter({3: 1})


# 统计在可迭代器中最常出现的元素
A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
A  # Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
A.most_common(1)  # [(3, 4)]
A.most_common(3)  # [(3, 4), (1, 2), (2, 2)]


# 两端都可操作的队列
Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
# deque([6, 5, 2, 1, 3, 4])
Q.pop()  # 4

Q.popleft() # 6

Q  # deque([5, 2, 1, 3])

Q.rotate(3)
Q.rotate(-3)


# 有最大长度的双端队列
last_three = collections.deque(maxlen=3)
for i in xrange(10):
    last_three.append(i)
    print ', '.join(str(x) for x in last_three)


#  可排序词典
m = dict((str(x), x) for x in range(10))
print ', '.join(m.keys())
# 1, 0, 3, 2, 5, 4, 7, 6, 9, 8

m = collections.OrderedDict((str(x), x) for x in range(10))
print ', '.join(m.keys())
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print ', '.join(m.keys())
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


# 默认词典
m = collections.defaultdict(int)
m = collections.defaultdict(str)
m = collections.defaultdict(lambda: '[default value]')


# 默认字典的简单树状表达
import json

tree = lambda: collections.defaultdict(tree)
root = tree()


# 对象到唯一计数的映射
import itertools, collections

value_to_numeric_map = collections.defaultdict(itertools.count().next)

value_to_numeric_map['a']  # 0
value_to_numeric_map['b']  # 1
value_to_numeric_map['c']  # 2


# 最大和最小的几个列表元素
a = [random.randint(0, 100) for __ in xrange(100)]

heapq.nsmallest(5, a)
heapq.nlargest(5, a)


# 两个列表的笛卡尔积
for p in itertools.product([1, 2, 3], [4, 5]):

for p in itertools.product([0, 1], repeat=4):
    print ''.join(str(x) for x in p)


# 列表组合和列表元素替代组合
for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print ''.join(str(x) for x in c)

for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print ''.join(str(x) for x in c)


# 列表元素排列组合
for p in itertools.permutations([1, 2, 3, 4]):
    print ''.join(str(x) for x in p)


# 可链接迭代器
a = [1, 2, 3, 4]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print p

for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1)):
    print subset


# 根据文件指定列类聚
import itertools

with open('contactlenses.csv', 'r') as infile:
    data = [line.strip().split(',') for line in infile]

data = data[1:]
def print_data(rows):
    print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in rows)

print_data(data)

data.sort(key=lambda r: r[-1])
for value, group in itertools.groupby(data, lambda r: r[-1]):
    print '-----------'
    print 'Group: ' + value
    print_data(group)











