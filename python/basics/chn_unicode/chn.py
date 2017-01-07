# -*- coding: utf-8 -*-

"""
python2 中文字符
"""

import os
import sys
import codecs


"""
前言:
其实内建的str和unicode和其它的Python内建类型(如: int, float, bool等等)一样都是class,
且它们俩个都是basestring的子类.
bytes和str是等价的, 其实它们就是同一个class.
"""

issubclass(str, basestring)      # True
issubclass(unicode, basestring)  # True

bytes is str  # True

isinstance('abc', str)       # True
isinstance('中文', str)      # True
isinstance(u'abc', unicode)  # True
isinstance(u'中文', unicode)  # True


bytes('abc') == 'abc'        # True
bytes('中文') == '中文'       # True
str('abc') == 'abc'          # True
str('中文') == '中文'         # True
bytes('abc') == str('abc')   # True
bytes('中文') == str('中文')  # True

#
# str
#

# 正确
str('abc')
str(1)
str(True)
str(None)

str(('a', u'中文'))
str(['a', u'中文'])
str({'a': u'中文', u'中文': 'b'})

# 错误
try:
    str(u'中文')
except UnicodeEncodeError as e:
    print e

#
# unicode
#

# 正确
unicode('abc')
unicode(u'abc')
unicode(u'中文')
unicode(1)
unicode(True)
unicode(None)

unicode(('a', u'中文'))
unicode(['a', u'中文'])
unicode({'a': u'中文', u'中文': 'b'})

# 错误
try:
    unicode('中文')
except UnicodeDecodeError as e:
    print e

# 上面的错误是因为, unicode的encoding参数没有指定,
# 所以它会按解释器的默认编码ascii去解码 > '中文' < 这个字节组,
# ascii编码无法解释 > '中文' < 所以报错
# 指定encoding参数为utf-8就不会报错了

unicode('中文', encoding='utf-8')  # 正确

try:
    unicode(u'中文', encoding='utf-8')
except TypeError as e:
    print e

#
# str和unicode的比较与相互转换
#

print '中文'.decode('utf-8') == u'中文'  # True

print u'中文'.encode('utf-8') == '中文'  # True


# 下面这行按理说不应该相等, 但它的结果确实是True
# 原因是python解释器对u'abc'做了隐式的转换
print 'abc' == u'abc'  # True

# 而下面这行就是False
# 原因是python解释器在试图转换u'中文'时会发生错误，但解释器并没有抛出这个异常
# 而是用UnicodeWarning代替. 然后返回结果False
print '中文' == u'中文'  # False

# 下面三行都是True, 原因同上, 隐式转换
unicode('abc') == 'abc'
unicode('abc') == str('abc')
unicode('abc') == bytes('abc')

#
# 常见错误
#

# 错误一
try:
    print '白雪 %s' % u'白雪'
except UnicodeDecodeError as e:
    print e
    # 这样就不会出错
    print '白雪 %s' % u'白雪'.encode('utf-8')
    print u'白雪 %s' % u'白雪'


# 错误二
try:
    print '白雪 %s' % u'白雪'
    print u'白雪 %s' % '白雪'
except UnicodeDecodeError as e:
    print unicode(e)
    # 这样就不会出错
    print '白雪 %s' % u'白雪'.encode('utf-8')
    print u'白雪 %s' % u'白雪'

try:
    u'白雪 {0}'.format('白雪')
except UnicodeDecodeError as e:
    print e

try:
    '白雪 {0}'.format(u'白雪')
except UnicodeEncodeError as e:
    print e


#
# 下面不会出错
#
print u'白雪 %s' % u'白雪'

print '白雪 %s' % '白雪'
