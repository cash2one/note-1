#!/usr/bin/env python
# -*- coding: utf-8 -*-
# applogconfig.py
#-----------------------------------------------------------------------------

import logging
import sys


# 设置消息格式
format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")

# 创建处理器，将CRITICAL级别的消息打印到stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)

# 创建处理器, 将消息打印到文件
applog_hand = logging.FileHandler("app.log")
applog_hand.setFormatter(format)

# 创建名为'app'的顶级记录器
app_log = logging.getLogger("app")
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

# 修改'app.net'记录器上的级别
logging.getLogger("app.net").setLevel(logging.ERROR)
