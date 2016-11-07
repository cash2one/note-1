# -*- coding: utf-8 -*-
import os
import logging


BASE_DIR = os.path.dirname(__file__)


"""
四个主要的组件:
logger: 日志类, 应用程序往往通过调用它提供的api来记录日志;
handler: 对日志信息处理, 可以将日志发送(保存)到不同的目标域中;
filter: 对日志信息进行过滤;
formatter: 日志的格式化;
"""

logging.basicConfig(
    # 设置日志的级别, 对低于该级别的日志消息将被忽略
    level=logging.DEBUG,
    # 日志文件的打开模式, 默认值为'a': 表示日志消息以追加的形式添加到日志文件中.
    # 如果设为'w', 那么每次程序启动的时候都会创建一个新的日志文件.
    filemode='w',
    # 指定handler使用的日志显示格式
    format='[%(asctime)s - %(levelname)-8s] %(name)s: %(message)s',
    # 定义日期格式
    datefmt='%Y-%m-%d %H:%M:%S',
    # 日志文件的保存路径. 如果配置了些参数, 将自动创建一个FileHandler作为Handler.
    filename=os.path.join(os.getcwd(), 'test.log'),
    # 用指定的stream创建StreamHandler. 可以指定输出到sys.stderr, sys.stdout或者文件, 默认为sys.stderr
    # 若同时列出了filename和stream两个参数, 则stream参数会被忽略.
    # stream=
)


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.debug('*********************')


# format参数中可能用到的格式化串:
# %(name)s             Logger的名字
# %(levelno)s          数字形式的日志级别
# %(levelname)s        文本形式的日志级别
# %(pathname)s         调用日志输出函数的模块的完整路径名, 可能没有
# %(filename)s         调用日志输出函数的模块的文件名
# %(module)s           调用日志输出函数的模块名
# %(funcName)s         调用日志输出函数的函数名
# %(lineno)d           调用日志输出函数的语句所在的代码行
# %(created)f          当前时间, 用UNIX标准的表示时间的浮点数表示
# %(relativeCreated)d  输出日志信息时的, 自Logger创建以来的毫秒数
# %(asctime)s          字符串形式的当前时间. 默认格式是 "2003-07-08 16:49:45,896" 逗号后面的是毫秒
# %(process)d          进程ID, 可能没有
# %(thread)d           线程ID, 可能没有
# %(threadName)s       线程名, 可能没有
# %(message)s          用户输出的消息


logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

logging.log(logging.WARNING, 'WARNING')
logging.exception('exception')
# 以ERROR级别记录日志消息, 异常跟踪信息将被自动添加到日志消息里. logging.exception通常用在异常处理块中


# 日志级别
# 可以给日志对象(Logger Instance)设置日志级别, 低于该级别的日志消息将会被忽略.
# 也可以给Hanlder设置日志级别, 低于该级别的日志消息, Handler也会忽略.
print logging.CRITICAL  # 50
print logging.ERROR     # 40
print logging.WARNING   # 30
print logging.INFO      # 20
print logging.DEBUG     # 10
print logging.NOTSET    # 0


# 获取日志级别对应的名称
print logging.getLevelName(logging.DEBUG)
print logging.getLevelName(10)


# 可用的Handler:
# logging.StreamHandler 可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
# logging.FileHandler 向一个文件输出日志信息
# logging.handlers.RotatingFileHandler 类似于上面的FileHandler,当文件达到一定大小之后,它会自动将当前日志文件改名,
#                                      然后创建一个新的同名日志文件继续输出
# logging.handlers.TimedRotatingFileHandler 和RotatingFileHandler类似,间隔一定时间就自动创建新的日志文件
# logging.handlers.SocketHandler 使用TCP协议,将日志信息发送到网络.
# logging.handlers.DatagramHandler 使用UDP协议,将日志信息发送到网络.
# logging.handlers.SysLogHandler 日志输出到syslog
# logging.handlers.NTEventLogHandler 远程输出日志到Windows NT/2000/XP的事件日志
# logging.handlers.SMTPHandler 远程输出日志到邮件地址
# logging.handlers.MemoryHandler 日志输出到内存中的制定buffer
# logging.handlers.HTTPHandler 通过"GET"或"POST"远程输出到HTTP服务器
