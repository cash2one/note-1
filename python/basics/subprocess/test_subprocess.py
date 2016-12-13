#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import subprocess


def dmi_info():
    return {
        'system': {
            'manufacturer': subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-manufacturer']).strip(),
            'product-name': subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-product-name']).strip(),
            'version': subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-version']).strip(),
            'serial-number': subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-serial-number']).strip(),
            'uuid': subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-uuid']).strip(),
        },
        'cpu': {
            'manufacturer': subprocess.check_output(['sudo', 'dmidecode', '-s', 'processor-manufacturer']).strip(),
            'version': subprocess.check_output(['sudo', 'dmidecode', '-s', 'processor-version']).strip(),
            'family': subprocess.check_output(['sudo', 'dmidecode', '-s', 'processor-family']).strip(),
        }
    }


def backup_database(host, port, user, passwd, db):
    proc = subprocess.Popen(
            ['mysqldump', '-h%s' % host, '--port=%s' % port,
             '-u%s' % user, '--password=%s' % passwd, db],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
    out, _ = proc.communicate()
    try:
        out = out[out.index(os.linesep)+1:]
    except ValueError:  # substring not found
        out = ''
    retcode = proc.poll()
    if retcode == 0:
        bak = os.path.join('/tmp/', 'bak-{0}-{1}.sql'.format(db, time.strftime('%Y%m%d%H%M%S')))
        f = open(bak, 'wb')
        f.write(out)
        f.close()
        return retcode, os.path.abspath(bak)
    else:
        return retcode, out


def execute_sql(host, port, user, passwd, db, sql_filename):
    """执行sql文件"""
    proc = subprocess.Popen(
            ['mysql', '--default-character-set=utf8', '-h', host,
             '--port=%s' % port, db, '-u', user, '--password=%s' % passwd],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT
        )
    # source 将文件中的内容读到stdin中执行
    # communicate执行一次就会结束掉process
    out, _ = proc.communicate('source ' + sql_filename)
    try:
        out = out[out.index(os.linesep)+1:]
    except ValueError:  # substring not found
        out = ''
    retcode = proc.poll()
    return retcode, out
