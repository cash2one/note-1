# -*- coding: utf-8 -*-

import os


os.listdir(dirname)  # 列出dirname下的目录和文件
os.getcwd()  # 函数得到当前工作目录，即当前Python脚本工作的目录路径
os.getenv()  # 读取环境变量
os.putenv()  # 设置环境变量
os.curdir  # 返回但前目录（’.')

os.chdir(dirname)  # 改变工作目录到dirname
os.sep  # 可以取代操作系统特定的路径分割符。
os.name  # 字符串指示你正在使用的平台。比如对于Windows，它是’nt’，而对于Linux/Unix用户，它是’posix’。
os.remove()  # 函数用来删除一个文件。
os.system()  # 函数用来运行shell命令。
os.linesep  # 字符串给出当前平台使用的行终止符。例如，Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’

os.makedirs(dirname)  # 创建多级目录,如:os.makedirs(‘/data/cc/ll/xx/zz’)
os.mkdir(path)  # 创建多级目录
os.rmdir(path)  # 删除目录 如:WIN: os.rmdir(‘E:\\book\\temp’) LINUX: os.rmdir(‘/data/cc’)


"""文件拷贝还可用shutil"""

import shutil

shutil.copyfile('listfile.py', 'd:/test.py')  # 复制文件
shutil.copystat(src, dst)  # 拷贝文件，连同文件的stat一起拷贝
shutil.copytree(src, dst)  # 拷贝目录，拷贝之前dst必须不存在
shutil.rmtree()  # 删除目录树
shutil.move()


"""os.path模块"""

os.path.isdir(name)  # 判断name是不是一个目录，name不是目录就返回false
os.path.isfile(name)  # 判断name是不是一个文件，不存在name也返回false
os.path.exists(name)  # 判断是否存在文件或目录name
os.path.abspath(name)  # 获得绝对路径
os.path.normpath(path)  # 规范path字符串形式
os.path.split(name)  # 分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext()  # 分离文件名与扩展名
os.path.join(path, name)  # 连接目录与文件名或目录
os.path.basename(path)  # 返回文件名
os.path.dirname(path)  # 返回文件路径

os.path.getsize(name)  # 获得文件大小（字节大小）如果name是目录返回0L
os.path.getctime(path)  # 返回浮点数的系统时间，在类Unix系统上是文件最近更改的时间， 在Windows上是文件或目录的创建时间
os.path.getmtime(path)  # 文件或目录最后更改的时间
os.path.getatime(path)  # 文件或目录最后存取的时间
os.path.samefile(path1, path2)  # 如果2个路径指向同样的文件或目录，返回True(Windows上不可用)


"""glob模块"""

import glob

glob.glob('*.py')  # 返回当前目录下所有以.py为后缀的目录或文件,glob(“*.py”) 里面可用正则去匹配,返回一个LIST列表.
