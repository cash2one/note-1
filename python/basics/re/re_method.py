# -*- coding: utf-8 -*-
import re

#
# 常用正则
#

# 邮箱地址
pattern = re.compile(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')


# re.match()
# re.search()
# re.findall()

#
# re.match – 匹配开始
# match()方法的工作方式是只有当被搜索字符串的开头匹配模式的时候它才能查找到匹配对象
#

match = re.match(r'dog', 'dog cat dog')  # 匹配成功
print match.group(0)

match = re.match(r'cat', 'dog cat dog')  # 匹配失败
if match:
    print match.group(0)


#
# re.search – 匹配任意位置
# search()方法和match()类似, 不过search()方法不会限制我们只从字符串的开头查找匹配
#

match = re.search(r'cat', 'dog cat dog')  # 匹配成功
print match.group(0)

#
# search()方法会在它查找到一个匹配项之后停止继续查找
# 因此在我们的示例字符串中用search()方法查找"dog"只找到其首次出现的位置
#

match = re.search(r'dog', 'dog cat dog')  # 匹配成功, 只匹配到第一个dog
print match.group(0)

#
# re.findall – 所有匹配对象
# 当我们调用findall()方法, 我们可以非常简单的得到一个所有匹配模式的列表, 而不是得到match的对象
#

print re.findall(r'dog', 'dog cat dog')


# match.start 和 match.end 方法
# search()和match()返回的"匹配对象", 实际上是一个关于匹配子串的包装类
# 先前你看到我可以通过调用group()方法得到匹配的子串
# (我们将在下一个部分看到, 事实上匹配对象在处理分组问题时非常有用)
# 但是匹配对象还包含了更多关于匹配子串的信息

# match对象可以告诉我们匹配的内容在原始字符串中的开始和结束位置
match = re.search(r'cat', 'dog cat dog')
print match.start()
print match.end()

#
# match.group() 通过数字分组
# match对象在处理分组时非常得心应手, 分组是对整个正则表达式的特定子串进行定位的能力
#

match = re.search(r'\w+, \w+: \S+', 'Doe, John: 555-1212-white')
if match:
    print match.group(0)

# 通过用圆括号来（字符'\'('和')'）包围正则表达式的特定部分, 我们可以对内容进行分组然后对这些子组做单独处理
match = re.search(r'(\w+), (\w+): (\S+)', 'Doe, John: 555-1212-white')
if match:
    print match.group(0)  # 所有匹配对象
    print match.group(1)
    print match.group(2)
    print match.group(3)


# 使用 match.group() 通过别名来分组
# Python还允许你通过下面的语句来指定一个组名:
match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', 'Doe, John: 555-1212-white')
if match:
    match.group('last')
    match.group('first')
    match.group('phone')


#
# 尽管findall()方法不返回分组对象, 它也可以使用分组.
# 类似的, findall()方法将返回一个元组的集合, 其中每个元组中的第N个元素对应了正则表达式中的第N个分组
#

print re.findall(r'(\w+), (\w+): (\S+)', 'Doe, John: 555-1212-white')


#
# 想要返回结果中包括整个匹配表达式, 就在整个reg外套上(), 返回的就包括整个字符串
#
processor_pattern = re.compile(r'(processor[ \t]+: \d+\n)')
s = 'someothers\n' \
    'processor : 12\n' \
    'hahahaha12\n'

print re.findall(processor_pattern, s)

# 如果只要数字
processor_pattern = re.compile(r'processor[ \t]+: (\d+)\n')

print re.findall(processor_pattern, s)
