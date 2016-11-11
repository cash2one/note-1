# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler


DEBUG = True

LOGFILE = 'log.log'
ERRFILE = 'error.log'
MAXBYTES = 12  # 12M -- 单个log文件的大小
BACKUPCOUNT = 8  # log文件备份数量


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)

verbose_formatter = logging.Formatter(
        fmt='[%(asctime)s - %(name)s - %(module)s - %(lineno)d] %(levelname)-8s\n%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

simple_formatter = logging.Formatter(
        fmt='[%(asctime)s - %(name)s] %(levelname)-8s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG if DEBUG else logging.INFO)
console_handler.setFormatter(simple_formatter)

file_handler = RotatingFileHandler(LOGFILE, maxBytes=1024*1024*MAXBYTES, backupCount=BACKUPCOUNT)
file_handler.setLevel(logging.DEBUG if DEBUG else logging.INFO)
file_handler.setFormatter(simple_formatter)

error_handler = logging.FileHandler(ERRFILE, mode='w')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(verbose_formatter)

if DEBUG:
    # 只有DEBUG=True时, 才将日志输出到console
    root_logger.addHandler(console_handler)

root_logger.addHandler(error_handler)
root_logger.addHandler(file_handler)
