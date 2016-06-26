#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


def backup_database(host, port, user, pwd, db):
    bak = 'bak-{0}-{1}.sql'.format(db, time.strftime('%Y-%m-%d-%H-%M-%S'))
    cmd = 'mysqldump -h{host} --port={port} -u{user} --password={pwd} {db} > {bak};'.format(
        host=host, port=port, user=user, pwd=pwd, db=db, bak=bak
    )
    ret = os.system(cmd)
    if ret:
        return ret
    else:
        return os.path.abspath(bak)


def execute_sql(host, port, user, pwd, db, sql):
    cmd = 'mysql -h{host} --port={port} -u{user} --password={pwd} {db} < {sql};'.format(
        host=host, port=port, user=user, pwd=pwd, db=db, sql=sql
    )
    return os.system(cmd)


if __name__ == '__main__':
    print backup_database('localhost', 3306, 'root', 'xuebailove321', 'marmot')
    # print execute_sql('localhost', 'root', 'xuebailove321', 'marmot', 'bak-marmot-2016-06-26-14-03-51.sql')
 
