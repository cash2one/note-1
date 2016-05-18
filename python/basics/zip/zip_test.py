#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import zipfile
import datetime


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for d in dirs:
                filelist.append(os.path.join(root, d))
            for f in files:
                filelist.append(os.path.join(root, f))            

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()
    return zipfilename


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
                os.mkdir(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def backup_dir(dirname):
    dt = datetime.datetime.now().strftime('-%y%m%d%H%M%S')
    base, name = os.path.split(dirname)
    print os.path.split(dirname)
    return zip_dir(dirname, os.path.join(base, 'bak'+name+dt+'.zip'))


if __name__ == "__main__":
    zip_dir('ice', 'ice.zip')
    # unzip('file.zip', 'file_zip')
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    # backup_dir(os.path.join(base_dir, 'ice'))
    # backup_dir('ice')
    # zfobj = zipfile.ZipFile('ice.zip')
    # for name in zfobj.namelist():
    #   if name.endswith('/'):
    #           print name

