#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc
from time import clock

starttime = clock()
print starttime

con = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=csms;UID=sa;PWD=123')

cursor = con.cursor()

cursor.execute("select*from admin")

results = cursor.fetchall()

for recordset in results:
    print recordset

cursor.close()

con.close()

endtime = clock()
print endtime

print endtime-starttime
