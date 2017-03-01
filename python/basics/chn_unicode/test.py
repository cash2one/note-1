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

print unicode('\u767d\u96ea')
