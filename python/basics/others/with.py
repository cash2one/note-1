#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""上下文管理器与with语句"""
import threading


# example-1
with open("debuglog", "a") as f:
    f.write("Debugging\n")
    # statements
    f.write("Done\n")

# example-2
lock = threading.Lock()
with lock:
    pass
    # 关键部分
    # statements
    # 关键部分结束

# 第一个例子中, 当控制流离开with语句后面的代码块时, with语句将自动关闭已打开的文件.
# 第二个例子中, 当控制流进入with语句后面的代码块是自动请求一个锁, 在控制流离开时又自动释放这个锁


if __name__ == "__main__":
    pass
