# -*- coding: utf-8 -*-

"""
brlog
version: 0.1
"""

import os
import logging.config


def config(logfilename=None, errfilename=None, debug=False):
    if logfilename is None:
        logfilename = os.path.join(os.getcwd(), 'base.log')
    if errfilename is None:
        errfilename = os.path.join(os.getcwd(), 'error.log')
    cf = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s - %(levelname)-8s] %(name)s : %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
            'simple': {
                'format': '[%(asctime)s] %(levelname)s : %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'filters': {
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',  # Null处理器传到/dev/null
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'common_file': {
                'level': 'DEBUG' if debug else 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': logfilename,                               # 日志文件名
                'maxBytes': 1024 * 1024 * 12,                          # 文件大小12M
                'backupCount': 8,                                      # 备份份数
                'formatter': 'verbose',                                # 日志格式
            },
            'error_file': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': errfilename,
                'maxBytes': 1024 * 1024 * 2,
                'backupCount': 2,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console', 'common_file', 'error_file'],
                'level': 'DEBUG' if debug else 'INFO',
                'propagate': True,
            },
        }
    }
    logging.config.dictConfig(cf)


logger = logging.getLogger('root')
