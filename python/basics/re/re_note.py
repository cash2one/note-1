#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""re note"""

import re


"""贪婪和非贪婪"""

html = 'Hello <a href="http://pypix.com" title="pypix">Pypix</a>'
m = re.findall('<a.*>.*<\/a>', html)
if m:
    print m  # ['<a href="http://pypix.com" title="pypix">Pypix</a>']


# 默认的匹配模式是"贪婪的"
# 当处于贪婪模式时, 量词(比如 * 和 +)匹配尽可能多的字符
html = 'Hello <a href="http://pypix.com" title="pypix">Pypix</a>' \
       'Hello <a href="http://example.com" title="example">Example</a>'
m = re.findall('<a.*>.*<\/a>', html)
if m:
    print m
    # 输出['<a href="http://pypix.com" title="pypix">Pypix</a>Hello <a href="http://example.com" title="example">Example</a>']


# 当你加一个问号在后面时(.*?)它将变为"非贪婪的"
m = re.findall('<a.*?>.*?<\/a>', html)
if m:
    print m  # 正确输出


"""前向界定符和后向界定符"""


strings = [
    "hello foo",     # returns False
    "hello foobar",  # returns True
]    

for string in strings:
    pattern = re.search(r'foo(?=bar)', string)
    if pattern:
        print 'True'
    else:
        print 'False'


strings = [
    "hello foo",    # returns True
    "hello foobar",  # returns False
    "hello foobaz",   # returns True
]

# 仅当它的后面没有跟着bar时才匹配
for string in strings:
    pattern = re.search(r'foo(?!bar)', string)
    if pattern:
        print 'True'
    else:
        print 'False'

# 后向界定符类似,但是它查看当前匹配的前面的模式.你可以使用 (?> 来表示肯定界定, (?<! 表示否定界定

# 下面的模式匹配一个不是跟在 foo 后面的 bar
strings = [
    "hello bar",     # returns True
    "hello foobar",  # returns False
    "hello bazbar",  # returns True
]      

for string in strings:
    pattern = re.search(r'(?<!foo)bar', string)
    if pattern:
        print 'True'
    else:
        print 'False'



"""条件(IF-Then-Else)模式"""

# 正则表达式提供了条件检测的功能,格式如下:
# (?(?=regex)then|else)

# 比如我们可以用这个正则表达式来检测打开和闭合的尖括号:
strings = [
    "<pypix>",  # returns true
    "<foo",     # returns false
    "bar>",     # returns false
    "hello",    # returns true
]

# 在下面的例子中, 1 表示分组 (<), 当然也可以为空因为后面跟着一个问号. 当且仅当条件成立时它才匹配关闭的尖括号.
for string in strings:
    pattern = re.search(r'^(<)?[a-z]+(?(1)>)$', string)
    if pattern:
        print 'True'
    else:
        print 'False'


"""
无捕获组
分组, 由圆括号括起来, 将会捕获到一个数组, 然后在后面要用的时候可以被引用. 但是我们也可以不捕获它们.
"""

string = 'Hello foobar'
pattern = re.search(r'(f.*)(b.*)', string)

print "f* => {0}".format(pattern.group(1))
# prints f* => foo    
print "b* => {0}".format(pattern.group(2))
# prints b* => bar

# 现在我们改动一点点，在前面加上另外一个分组 (H.*)
string = 'Hello foobar'
pattern = re.search(r'(H.*)(f.*)(b.*)', string)
print "f* => {0}".format(pattern.group(1))
# prints f* => Hello
print "b* => {0}".format(pattern.group(2))
# prints b* => bar

# 如果我们真的对一个新添加的分组的内容没兴趣的话, 我们可以使它"不被捕获", 就像这样
string = 'Hello foobar'
pattern = re.search(r'(?:H.*)(f.*)(b.*)', string)
print "f* => {0}".format(pattern.group(1))
# prints f* => foo
print "b* => {0}".format(pattern.group(2))
# prints b* => bar


"""命名组"""


string = 'Hello foobar'
pattern = re.search(r'(?P<fstar>f.*)(?P<bstar>b.*)', string)
print "f* => {0}".format(pattern.group('fstar'))
# prints f* => foo
print "b* => {0}".format(pattern.group('bstar'))
# prints b* => bar


"""
使用回调函数
在 Python 中 re.sub() 可以用来给正则表达式替换添加回调函数
"""


template = "Hello [first_name] [last_name], \
Thank you for purchasing [product_name] from [store_name]. \
The total cost of your purchase was [product_price] plus [ship_price] for shipping. \
You can expect your product to arrive in [ship_days_min] to [ship_days_max] business days. \
Sincerely, \
[store_manager_name]"

# assume dic has all the replacement data
# such as dic['first_name'] dic['product_price'] etc...

dic = {
    "first_name": "John",          
    "last_name": "Doe",          
    "product_name": "iphone",          
    "store_name": "Walkers",          
    "product_price": "$500",          
    "ship_price": "$10",          
    "ship_days_min": "1",          
    "ship_days_max": "5",          
    "store_manager_name": "DoeJohn",     
}

result = re.compile(r'<p style="text-align:center;"><span class="MathJax_Preview">\[(.*)\]</span><script type="math/tex;  mode=display">(.*)</script></p>')          
print result.sub('John', template, count=1)


template = "Hello [first_name] [last_name], \
 Thank you for purchasing [product_name] from [store_name]. \
 The total cost of your purchase was [product_price] plus [ship_price] for shipping. \
 You can expect your product to arrive in [ship_days_min] to [ship_days_max] business days. \
 Sincerely, \
 [store_manager_name]"

# assume dic has all the replacement data
# such as dic['first_name'] dic['product_price'] etc...

dic = {          
    "first_name": "John",
    "last_name": "Doe",
    "product_name": "iphone",
    "store_name": "Walkers",
    "product_price": "$500",
    "ship_price": "$10",
    "ship_days_min": "1",
    "ship_days_max": "5",
    "store_manager_name": "DoeJohn",      
}

def multiple_replace(dic, text):
    pattern = "|".join(map(lambda key : re.escape("["+key+"]"), dic.keys()))
    return re.sub(pattern, lambda m: dic[m.group()[1:-1]], text)

print multiple_replace(dic, template)



#
m = re.search('^The', 'The end.')
if m:
    m.group()

m = re.search('^The', 'end. The')


# \b 边界
m = re.search('\bthe', 'bite the dog')
if m:
    m.group()  # >>> 'the'

m = re.search('\bthe', 'bitethe dog')
if m:
    m.group()  # >>> None

m = re.search('\Bthe', 'bitethe dog')
if m:
    m.group()  # >>> 'the'


# sub()和subn()
re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
# >>> 'attn:Mr. Smith\n\nDear Mr. Smith,\n'


re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
# >>> ('attn:Mr. Smith\n\nDear Mr. Smith,\n', 2)


# re.split()


if __name__ == "__main__":
    pass
