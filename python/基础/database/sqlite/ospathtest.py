#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: ospathtest.py
# Created: 17/12/2013 10:31:49
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

import os
import time


dataPath = os.getcwd()+r'\data'
print dataPath
ok = os.path.exists(dataPath)
print ok
if not ok:
    os.mkdir(dataPath)
    
datetime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
sql = '%s\%s.db' % (dataPath, datetime)
print sql
