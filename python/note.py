# -*- coding: utf-8 -*-

#*******************************************************************************
# 实用函数, 操作符, 技巧, 注意
#*******************************************************************************
"""
__doc__变量; 在模块, 类和函数声明中第一个没有赋值的字符串, 即文档字符串. 可以用obj.__doc__来访问
template.py -- sample module demonstrating documentation strings
在导入模块时, 可以通过模块, 类和函数的__doc__属性来访问它的docstirng

\ --  继续上一行
; --  同一行书写多个语句可以用;分隔
"""

"\"--继续上一行"
";"--同一行书写过个语句可以用";"分隔
"_"--在解释器中有特别含义，表示最后一个表达式的值

#专用下划线标示符
_xxx -- 不被'from module import *'导入
_xxx_ -- 系统定义名字
_xxx -- 类中的私有变量名
"__xxx__"对python有特殊意义,所以应避免对普通变量采用这种命名风格


print 语句是调用的str()来输出的
在交互式解释器中是调用的repr()

print "%s is number %d and %f" % ("Python", 1, 1.2)

# >> -- 用来重定向输出
# 将输出重定向到标准错误输出
import sys
print >> sys.stderr, 'Fatal error: invalid input!'

#将输出重定向到日志文件
logfile = open('/tmp/mylog.txt', 'a')
print >> logfile, 'Fatal error: invalid input!'
logfile.close()

raw_input('your string:')

help(raw_input)

"/"--传统除法,地板除
"//"--浮点除法,真正的除法
"%"--取余

and, or , not

del---删除对象

#---实用函数
dir(obj) --- 显示对象属性
help(obj) --- 显示对象的文档字符串
globals() --- 返回调用者全局和局部名称空间的字典
locals() ---
##################工厂函数
int(obj) --- 工厂函数
list() --- 工厂函数
dict()
tuple()
bool()
float()
long()
complex()
unicode()
set(),frozenset()
object()
classmethod()
staticmethod()
super()
property()
file()
basestring() --- 抽象工厂函数
#################
len(obj)----参数只能接受序列类型
reversed()----参数只能接受序列类型
sum()----参数只能接受序列类型

open(fn, AccessMode)
range(start, stop, step=1)----start<=k<stop,k每次递增step
xrange()----很大范围列表时，用xrange()更合适，不过只能在for中使用它
raw_input(str)
str(obj)
repr(obj)---返回对象的字符表示
type(obj)---返回对象的类型的type对象
id(obj)---获取对象身份

isinstance()---isinstance(num,(int,long,float,complex)) >> bool

#数值运算函数
cmp(obj1, obj2)---返回整型比较结果;obj1<obj2 >> 负整型
                                obj1=obj2 >> 0
                                obj1>obj2 >> 正整型
eval()----求值运算符

pow(x,y)----等价于x**y


coerce()----明确指定对某种数据类型进行特殊类型转换
            它不依赖python解释器
            返回一个包含类型转换完毕的两个数值元素的元组
            对于一种新建的数值类型来说，这个特性非常有用

divmod()----返回一个包含商和余数的元组
            对于浮点数来说math.floor(num1/num2)
            对于复数ath.floor((num1/num2).real)

round()----对浮点数四舍五入
            例子round（3）>> 3.0
            round(3.49) >> 3.0
            round(3.499, 1) >> 3.5

#----进制转换函数
hex()----16进制
oct()----8进制
ord()----ASCII码
chr()----单字节整形值，返回字符串
unichr()----接受Unicode码值，返回对应Unicode字符

#---技巧

#交互两个变量的值
x, y = y, x
#多重赋值
x = y = z = 1
#多元赋值
x,y,z = 1,2,'string'

#多个比较操作符
3<4<7  same as (3<4) and (4<7)

#对象引用
foo1 = foo2 = 4.3 或foo1 = 4.3; foo2 = foo1
实际foo1和foo2指向的是同一个对象

foo1 = 4.3
foo2 = 1.3+3.0
这样它们两个就指向不同的对象

可以用is 和 is not 来测试两个对象是不是指向同一个对象
foo1 is foo2
等价于 id(foo1) == id(foo2)

#成员关系操作符
in  , not in

#实用局部变量替换模块变量可以提高效率
#调试器---pdb
#记录器---logging
#性能测试器---profile、hotshot、cProfile


##################################################################################
# 基本数据类型
##################################################################################

# python 没有字符类型char或byte
# 五种基本类型
int
long
bool
float
complex

# 后面加个L表示long类型---1L

# 第六种类型 decimal -- 用于十进制浮点型, 它不是内建类型，需要import decimal模块

#----------序列

>>s = 'abcdefgh'
>>s[::-1]----可视作翻转操作符
'hgfedcba'
>>s[::2}----隔一个取一个

>>> range(-6, -1)
[-6, -5, -4, -3, -2]
>>> range(-1,-6,-1)
[-1, -2, -3, -4, -5]
>>> range(1,6)
[1, 2, 3, 4, 5]
>>> range(6,1,-1)
[6, 5, 4, 3, 2]


#序列类型可用的内建函数
len()
enumerate()
max()
min()
reversed()
sorted()
sum()
zip()

#-----------------字符串
pystr = 'python'
pystr * 2
'pythonpython'

'-' * 20
'-----------------'

r'\n'----表示原始字符串(即不包括转义字符或不能打印的字符)
u'string'----unicode字符
"""__"""----三引号字符串中可以包含换行符、制表符等特殊字符

#字符串Template对象
from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lange='Python', howmany=3)
'there are 3 Python Quotation Symbols'

#字符串内建方法
见P146

#-----------------元组
--元素类型可以不同,不可改变;可以看成是只读的列表
tuple
aTuple = (1,'2',3,4)
可以通过索引和切片运算([]和[:])得到子集也是元组
单个元素的元组
(1,)

可以用list(tuple)将一个元组转换成list
#-----------------列表
list
aList = ['123',2,3,'4']

del aList[1]----删除列表元素
aList.remove('4')
aList.pop()----删除并返回一个特定对象
aList.append()----向list中添加一个对象
aList.count(obj)----返回一个对象在列表中出现的次数
aList.extend(seq)----把序列seq的内容添加到列表中
aList.insert(index, obj)
aList.index(obj, i=0, j=len(list))
aList.reverse()----原地翻转列表
aList.sort(func=None, key=None, reverse=False)----指定方式排序列表成员
#那些可以改变对象值的可变对象的方法是没有返回值的
像sort(), extend(), reverse()这些方法是没有返回值的，只在原地改变对象的值的

不过2.4以后加入的reversed()和sorted()内建函数，是有返回值的,不会改变原来的对象

aList[:]----表示返回整个序列的一个浅拷贝
"+"----用来连接序列效率不高,尽量用字符串格式化操作符(%s),join(['foo','bar'])来取代.
对于列表来说，extend方法可以把另一个列表中的内容加进来list1.extend(list2)

#-----------------字典
dict
aDict = {1:'1', '2':2, 'port':80}

>>aDict.keys()
[1,'2','port']
>>aDict.values()
['1', 2, 80]
>>aDict['2']
2
aDict.items()----返回一个包含字典中键、值对元组的列表
aDict.update(dict2)----将字典dict2中的键-值对添加到字典aDict中
aDict.clear()----删除字典中的所有条目

>>for key in aDict
..print key, aDict[key]

#类型对象
类型也是一个对象type(obj)

#特殊类型
Null对象它只有一个值---None,类似与C中的void
None的布尔值总是False

#每个对象天生具有布尔值True和False
空对象，值为0的任何数字或Null对象None的布尔值都是False

dict9 = dict8.copy()---这样得到dict9效率更好

hash()----判断是不是可hash对象



#------------------------集合

set可变集合
frozenset不可变集合

利用其工厂函数set()和frozenset()是创建集合唯一的方法








#-------------------------------流程控制语句------------------------------

#选择语句
C/C++ :: C?X:Y
python :: X if C else Y

break----跳出循环
continue----立即结束本次循环，进入下一次循环

可以在while和for循环中使用else语句,它只在循环或迭代完成后执行，也就是说，使用break
也会跳过它

# ---if---
if expression1:
    if_suite
elif expression2:
    elif_suite
else:
    else_suite


# ---while---
while expression:
    while_suite



# ---for---
for item in ['e-mail', 'net-surfing', 'homework']

range(3)
len('abcdefg')

enumerate---是一个能让你同时迭代和计数的内置函数
data = (123, 'abc', 3.123)
for i, value in enumerate(data):
    print i, value
0 123
1 'abc'
2 3.123

#-----迭代器
itertools模块----它提供了各种有用的迭代器
例：
myTuple = (123, 'xyx', 45.88)
i = iter(myTuple)
>>i.next()
123
>>i.next()
'xyz'
>>i.next()
45.88
>>i.next()
Except

#列表解析p229
>>squared = [x**2 for x in range(4)]
[0,1,4,9]

>>squared = [x**2 for x in range(8) if not x%2]
[0,4,16,36]



open()和file()内建函数
file()和open()功能一样但file()更确切表明它是个工厂函数

#生成器表达式----懒惰的列表解析
(expr for iter_var in iterable if cond_expr)



#-------------------------------错误和异常------------------------------

#标准异常列表P279

触发异常
raise[someException [, args [, traceback]]]


try:
    suit
except IOError, e:
    suit
except Exception, e:
    suit
else:
    suit ----try中的语句没有异常的执行完，才执行
finally:
    suit ----无论try中语句是否执行完，finally都将执行



try:
    suit
finally:
    suit----无论try中语句是否执行完，finally都将执行
            即：当try中发生异常时，会先执行finally子句后，在返回异常


try:
    try:
        suit
    except:
        suit
finally:
    suit


#上下文管理
with 语句----是用来简化代码的
try--except和try--finally的一种特定的配合用法是保证共享资源的唯一分配，并在任务结束后释放它
比如文件、线程资源，简单同步、数据库连接等等，with语句就是应用在这种场景

例：
with open('filename', 'r') as f:
    for eachLine in f:
        suit
它尝试打开一个文件，如成功就把文件对象赋给f，然后执行处理，完成后关闭文件.
无论这段代码是在开始、中间、还是结束时发生异常，会执行清理的代码，然后文件会自动关闭.


#异常和sys模块
sys.exc_info()----返回一个关于异常的3元组:
                  exc_type异常类;exc_value异常类实例;exc_traceback跟踪记录




#--------traceback模块

#------------------------------函数----------------------------

如果函数中没有return语句，会自动返回None对象

python是通过引用调用的，意味着函数内对参数的改变会影响原始对象，不过事实上只有可改变的
对象会受影响，对于不可变对象，行为类似按值调用

def function_name([arguments = DefaultValue]):
    "DocString"
    function_suite
    return x

python中定义函数时没有返回类型，在return后随便写就行了，可以返回多个值return x, y, 'z'

#参数组
func(postitional_args, keyword_args, *tuple_grp_nonkw_args, **dict_grp_kw_args)

#函数和方法装饰器p300

使用装饰器就是在现有的功能上再"加盖"额外的功能

静态方法
class myClass(object):
    def staticFoo():
        staticFoo = staticmethod(staticFoo)

class myClass(object):
    @staticmethod----方法装饰器声明staticFoo()为静态方法
    def staticFoo():
        suit

    @classmethod
    def classFoo(cls):
        suit

#函数式编程
lambda [arg1,[,arg2,....argn]} : expression


#生成器p329

#---------------------------类------------------------------------

class ClassName(base_class[es]):
    "DocString"
    static_member_declarations
    method_declarations


例子：
class FooClass(object):
    """my first class: FooClass"""
    version = 0.1  #静态变量
    
    def __init__(self, nm=='John Doe'):
        """constructor"""
        self.name = nm

    def showname(self):
        """xxxxxxx"""
        print 'Your name is', self.name
        print 'My name is', self.__class__.__name__


#---------------------------模块---------------------------

write()不同于print 它不会再字符串后面添加换行符


#常用模块
高级数字科学计算：Numeric(NumPy) 和 SciPy

os----有助于跨平台开发的模块,对于文件系统的访问大多通过os模块实现
os.path----
sys----
pickle 和 marshal ----永久存储模块
decimal----十进制浮点运算类
array----高效数值数组(字符、整型、浮点型等)
math/cmath----标准c库数学运算函数,常用数学运算在math模块，复数运算在cmath模块
operator----数字操作符的函数实现
random----多种伪随机数生成器


#---------------------------文件对象----------------------------
    文件对象不仅可以用来访问普通的磁盘文件，也可以访问任何其他类型抽象层面上的"文件".
一旦设置好合适的"钩子"，就可以访问具有文件类型接口的其他对象.
例如：打开一个URL来读取Web界面;
     在另一个独立的进程中执行一个命令进行通信;

file_obj = open(file_name, access_mode='r', buffering=-1)
file()
一般建议使用open()


file_obj.read(size=-1)----直接读取字节到字符串，最多读取给定数目个字节,默认-1读到末尾
file_obj.readline(size=-1)----如果给定size参数，那么超过size的行会返回不完整行
file_obj.readlines(sizhint)----它会返回所有剩余行

file_obj.write()
file_obj.writelines()
file_obj.flush----直接把内部缓冲区中的数据立即写入文件
file_obj.truncate()----截取到最多size字节处

file_obj.seek(args)----在文件中移动文件指针,args:0,1,2==SEEK_SET,SEEK_CUR,SEEK_END
file_obj.tell()----返回文件指针当前的位置


sys.argv----命令行参数的列表;sys.argv[0]是程序的名字
