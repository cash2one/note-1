# -*- coding: utf-8 -*-
import os
import logging


logger = logging.getLogger('root')


# 多次使用相同名称来调用getLogger, 返回的是同一个对象的引用
# Logger实例之间有层次关系, 这些关系通过Logger名称来体现
root = logging.getLogger('root')
c1 = logging.getLogger('root.child1')
c2 = logging.getLogger('root.child2')
# root是父logger, c1, c2分别是root的子logger. c1, c2将继承root的设置. c1, c2的日志自己处理完还会交给父级logger再处理
# 如果省略了name参数, getLogger将返回日志对象层次关系中的根Logger(root)


# logger.setLevel(level)


try:
    raise ValueError('this is a exception')
except Exception as e:
    logger.exception('exception')  # 异常信息被自动添加到日志消息中


# logging.setLoggerClass()
# logging.getLoggerClass()
# 获取/设置日志类型. 用户可以自定义日志类来代替系统提供的logging.Logger类


# Logger.addFilter(filter)
# Logger.removeFilter(filter)
# 添加/移除日志消息过滤器


# Logger.addHandler(handler)
# Logger.removeHandler(handler)
# 添加/移除日志消息处理器


# Logger.makeRecord(name, lvl, fn, lno, msg, args, exc_info[, func, extra])
# 创建LogRecord对象. 日志消息被实例为一个LogRecord对象, 并在日志类内处理.


# logging.shutdown()
# 当不再使用日志系统的时候, 调用该方法, 它会将日志flush到对应的目标域上. 一般在系统退出的时候调用.
