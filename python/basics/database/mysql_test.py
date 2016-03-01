#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''测试mysql操作'''

__author__ = 'Pysaoke'


import MySQLdb


try:
    conn=MySQLdb.connect(host='localhost', user='root', passwd='xuebailove321', db='crm', port=3306)
    cur=conn.cursor()
    cur.execute('select * from accounts_zone')
    print cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# try:
#     conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
#     cur=conn.cursor()

#     cur.execute('create database if not exists python')
#     conn.select_db('python')
#     cur.execute('create table test(id int,info varchar(20))')

#     value=[1,'hi rollen']
#     cur.execute('insert into test values(%s,%s)',value)

#     values=[]
#     for i in range(20):
#         values.append((i,'hi rollen'+str(i)))

#     cur.executemany('insert into test values(%s,%s)', values)
 
#     cur.execute('update test set info="I am rollen" where id=3')

#     conn.commit()  # 这句来提交事务，要不然不能真正的插入数据
#     cur.close()
#     conn.close()

# except MySQLdb.Error,e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# try:
#     conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
#     cur=conn.cursor()
     
#     conn.select_db('python')
 
#     count=cur.execute('select * from test')
#     print 'there has %s rows record' % count
 
#     result=cur.fetchone()
#     print result
#     print 'ID: %s info %s' % result
 
#     results=cur.fetchmany(5)
#     for r in results:
#         print r
 
#     print '=='*10
#     cur.scroll(0,mode='absolute')
 
#     results=cur.fetchall()
#     for r in results:
#         print r[1]

#     conn.commit()
#     cur.close()
#     conn.close()
 
# except MySQLdb.Error,e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


