#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: sqlite.py
# Created: 16/12/2013 15:01:00
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

import sqlite3
import time
import os


class DataBase(object):

    def __init__(self):
        super(DataBase, self).__init__()
        #验证data目录，没有就创建它
        datetime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        self.dataPath = os.getcwd()+r'\data'
        self.createDataDir()   
        sql = '%s\%s.db'%(self.dataPath,datetime)
        #创建已当前时间命名的数据库文件
        self.conn = sqlite3.connect(sql)
        self.cur = self.conn.cursor() 
        #创建表
        sql_createTable = "CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, ash FLOAT, com FLOAT)"
        self.cur.execute(sql_createTable)

    def createDataDir(self):
        '创建data文件夹，如果存在就忽略'
        if not os.path.exists(self.dataPath):
            os.mkdir(self.dataPath)

    def insert(self, ash, com):
        self.cur.execute("INSERT INTO data VALUES(NULL,%s,%s)" % (ash,com))
        self.conn.commit()

    def getAll(self):
        self.cur.execute("select ash,com from data")
        data = self.cur.fetchall()
        ash = [i[0] for i in data]
        com = [i[1] for i in data]
        return ash, com
    

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = DataBase()
    for i in range(0,100):
        db.insert(12.5, 13.5)
    ash,com = db.getAll()
    print ash,com
    db.close()











        
