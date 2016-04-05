# -*- coding: utf-8 -*-
import logging
import dict_config


base_logger = logging.getLogger('base_log')
custom_logger = logging.getLogger('base_log.custom')


custom_logger.debug('debug')
custom_logger.info('info')
custom_logger.warning('warning')
custom_logger.error('error')
custom_logger.critical('critical')
