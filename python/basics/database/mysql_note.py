#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 常用函数

# commit() 提交
# rollback() 回滚

# cursor用来执行命令的方法:
# callproc(self, procname, args):用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
# execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
# nextset(self):移动到下一个结果集

# cursor用来接收返回值的方法:
# fetchall(self):接收全部的返回结果行.
# fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# fetchone(self):返回一条结果行.
# scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条. 

import time, MySQLdb

# 连接
conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库.
data = cursor.fetchone()

# 关闭数据库连接
conn.close()

# show databases and show tables
conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
cur=conn.cursor()

cur.execute('show databases')
cur.execute('show tables')

# create database
cur.execute('create database if not exists python')
conn.select_db('python')

# 删除表
sql = "drop table if exists user"
cursor.execute(sql)

# 创建
sql = "create table if not exists user(name varchar(128) primary key, created int(10))"
cursor.execute(sql)

# 写入
sql = "insert into user(name,created) values(%s,%s)"
param = ("aaa", int(time.time()))
n = cursor.execute(sql, param)
print 'insert', n

# 写入多行
sql = "insert into user(name,created) values(%s,%s)"
param = (("bbb", int(time.time())), ("ccc", 33), ("ddd", 44) )
n = cursor.executemany(sql, param)
print 'insertmany', n

# 更新
sql = "update user set name=%s where name='aaa'"
param = ("zzz")
n = cursor.execute(sql,param)
print 'update', n

# 删除
sql = "delete from user where name=%s"
param =("bbb")
n = cursor.execute(sql,param)
print 'delete', n

# 查询
n = cursor.execute("select * from user")
print cursor.fetchall()

cursor.close()

# 提交
conn.commit()
# 关闭
conn.close()