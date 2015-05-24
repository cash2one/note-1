#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image


def add_thumb(s):
    '''
    例:"rabbit.jpg"上传后得到的预览文件名就是"rabbit.thumb.jpg"
    '''
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'

    return ".".join(parts)

path = '4.jpg'

img = Image.open(path)

img.thumbnail((128, 128), Image.ANTIALIAS)

img.save(add_thumb(path), 'JPEG')



if __name__ == "__main__":
    pass
