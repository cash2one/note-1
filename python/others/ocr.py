#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
验证码识别
"""

from PIL import Image
from pytesseract import image_to_string


im = Image.open('/home/baixue/idea/python/ocr/image_login.jpg')
imgry = im.convert('L')  # 转化灰度图

# 把图像中的噪声去除掉,图像比较简单,直接阈值化就行了.把大于阈值threshold的像素置为1,其他的置为0.先生成一张查找表
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = imgry.point(table, '1')

# 把图片中的字符转化为文本
text = image_to_string(out)

print text
