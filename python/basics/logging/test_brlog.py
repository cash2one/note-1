# -*- coding: utf-8 -*-
import logging


root_logger = logging.getLogger()

root_logger.setLevel(logging.DEBUG)

verbose_formatter = logging.Formatter(
        fmt='[%(asctime)s - %(levelname)-8s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

simple_formatter = logging.Formatter(
        fmt='[%(asctime)s]%(levelname)-8s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(simple_formatter)

file_handler = logging.FileHandler('project.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(verbose_formatter)

error_handler = logging.FileHandler('error.log', mode='w')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(verbose_formatter)

root_logger.addHandler(error_handler)
root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)
