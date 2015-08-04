#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name: pymssqlTest.py
#
# Purpose: 测试 pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
#
# Author: scott
#
# Created: 04/02/2012
#-------------------------------------------------------------------------------
import pyodbc

con = pyodbc.connect('''DRIVER={SQL Server};
	SERVER=localhost;DATABASE=djangodb;UID=sa;PWD=7552735535''')
cur = con.cursor()
cur.execute("select* from auth_user")
print con
for row in cur:
        print 'Title:'+row.title,'content:'+row.content
