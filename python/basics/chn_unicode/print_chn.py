# -*- coding: utf-8 -*-

"""
python2 unicode字符
"""

import os


print '白雪'

print '白雪'.decode('utf-8') == u'白雪'  # True

print u'白雪'

print u'白雪'.encode('utf-8') == '白雪'  # True


bytes('abc') == 'abc'        # True
bytes('中文') == '中文'       # True
bytes('abc') == str('abc')   # True
bytes('中文') == str('中文')  # True

# 下面这行按理说不应该相等, 但它的结果确实是True
# 原因是python解释器对u'abc'做了隐式的转换
'abc' == u'abc'  # True

# 而下面这行就是False
# 原因是python解释器在试图转换u'中文'时会发生错误，但解释器并没有抛出这个异常
# 而是用UnicodeWarning代替. 然后直接返回结果False
'中文' == u'中文'  # False


# 内建的unicode()函数：将一个string类型的字符串转变成一个unicode对象

# 下面三行都是True, 原因同上, 隐式转换
unicode('abc') == 'abc'
unicode('abc') == str('abc')
unicode('abc') == bytes('abc')





unicode('中文')


#
# 错误一
#
try:
    print '白雪 %s' % u'白雪'
except UnicodeDecodeError as e:
    print unicode(e)
    # 这样就不会出错
    print '白雪 %s' % u'白雪'.encode('utf-8')
    print u'白雪 %s' % u'白雪'


#
# 错误二
#
try:
    print '白雪 %s' % u'白雪'
except UnicodeDecodeError as e:
    print unicode(e)
    # 这样就不会出错
    print '白雪 %s' % u'白雪'.encode('utf-8')
    print u'白雪 %s' % u'白雪'





#     print u'白雪 {0}'.format('白雪')
#     print u'白雪 %s' % '白雪'
# except UnicodeError as e:
#     print unicode(e)


# try:
#     str(u'白雪')
# except UnicodeEncodeError as e:
#     print unicode(e)


#
# 下面不会出错
#
# print u'白雪 %s' % u'白雪'

# print '白雪 %s' % '白雪'


