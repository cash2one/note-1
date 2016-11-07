# -*- coding: utf-8 -*-
import logging
import dict_config


base_logger = logging.getLogger('base_log')
custom_logger = logging.getLogger('base_log.custom')


base_logger.debug('debug')
base_logger.info('info')
base_logger.warning('warning')
base_logger.error('error')
base_logger.critical('critical')
