# -*- coding: utf-8 -*-
import os
import logging.config


CONF = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s - %(levelname)-8s] %(name)s: %(message)s',
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
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.getcwd(), 'custom.log'),   # 日志文件
            'maxBytes': 1024 * 1024 * 20,                          # 文件大小20M
            'backupCount': 8,                                      # 备份份数
            'formatter': 'verbose',                                # 日志格式
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.getcwd(), 'error.log'),
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'base_log': {
            'handlers': ['common_file', 'error_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'base_log.custom': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

logging.config.dictConfig(CONF)
