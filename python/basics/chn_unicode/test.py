# -*- coding: utf-8 -*-

"""
翻译Unicode码点
"""

import os
import sys
import codecs
import unicodedata


print u'\u767d\u96ea'

print unichr(0x767d)
print unichr(0x767d).encode('utf-8')
print unichr(int('fd9b', 16)).encode('utf-8')


print u'\u767d\u96ea'

print u'\u767d\u96ea'.encode('utf-8')
print u'白雪'.encode('utf-8')

print u'\u767d\u96ea' == u'白雪'  # True

print u'白雪'.encode("unicode_escape")

print '\u767d\u96ea'.decode('unicode_escape') == u'白雪'  # True
