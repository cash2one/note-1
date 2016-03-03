#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''python 随机数与随机字符'''

__author__ = 'baixue'

import random


# 随机整数
random.ran(0,99)

# 随机0-100之间的偶数
random.randrange(0, 101, 2)

# 随机浮点数
random.random()
random.uniform(1, 10)

# 随机字符
random.choice('abcdefg!@#$%^&')

# 多个字符中选取特定数量的字符
random.sample('abcdefghij', 3)

# 多个字符中选取特定数量的字符组成新字符串
import string
string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).replace(" ","")

# 洗牌
items = range(1, 10)
random.shuffle(items)
print items


if __name__ == "__main__":
    pass
