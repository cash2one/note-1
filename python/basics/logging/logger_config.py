# -*- coding: utf-8 -*-
import logging


formatter = logging.Formatter(
        fmt='[%(asctime)s] %(levelname)s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('test.log', mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


root_logger = logging.getLogger('root')
app_logger = logging.getLogger('root.app')


root_logger.setLevel(logging.INFO)
root_logger.addHandler(file_handler)

app_logger.setLevel(logging.DEBUG)
app_logger.addHandler(console_handler)

app_logger.debug('debug')
app_logger.info('info')
app_logger.warning('warning')
app_logger.error('error')
app_logger.critical('critical')
