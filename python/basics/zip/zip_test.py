#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import zipfile
import shutil
import datetime


# shutil.make_archive('xxx.zip', 'zip', 'xxx')


def zipdir(dirname, zipfilename=None):
    if zipfilename is None:
        zipfilename = os.path.basename(os.path.normpath(dirname)) + '.zip'
    zipf = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED)
    base_len = len(dirname)
    for root, dirs, files in os.walk(dirname):
        for f in files:
            fn = os.path.join(root, f)
            zipf.write(fn, fn[base_len:])
        for d in dirs:
            fn = os.path.join(root, d)
            zipf.write(fn, fn[base_len:])
    zipf.close()


def unzip(filename, to_dir):
    if not zipfile.is_zipfile(filename):
        raise ValueError('%s is not zip-file or not exist' % filename)
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    zfobj = zipfile.ZipFile(filename)
    for name in zfobj.namelist():
        if name.endswith('/'):
            os.mkdir(os.path.join(to_dir, name))
        else:
            ext_filename = os.path.join(to_dir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def backup_dir(dirname):
    dt = datetime.datetime.now().strftime('-%y%m%d%H%M%S')
    base, name = os.path.split(dirname)
    print os.path.split(dirname)
    return zipdir(dirname, os.path.join(base, 'bak'+name+dt+'.zip'))


if __name__ == "__main__":
    import time
    st = time.time()
    # shutil.make_archive('/home/pysaoke/idea/react.zip', 'zip', '/home/pysaoke/idea/react')
    # zipdir('/home/pysaoke/idea/django', '/home/pysaoke/idea/django.zip')
    zip_ref = zipfile.ZipFile('/home/pysaoke/idea/django.zip', 'r')
    zip_ref.extractall('/home/pysaoke/idea/djangozip')
    zip_ref.close()
    print time.time() - st
    # shutil.make_archive('/home/pysaoke/idea/python.zip', 'zip', '/home/pysaoke/idea/python')
    # unzip('file.zip', 'file_zip')
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    # backup_dir(os.path.join(base_dir, 'ice'))
    # backup_dir('ice')
    # zfobj = zipfile.ZipFile('ice.zip')
    # for name in zfobj.namelist():
    #   if name.endswith('/'):
    #           print name
