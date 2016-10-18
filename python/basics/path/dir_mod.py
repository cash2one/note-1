#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pwd
import stat
import getpass


os.access('/path', os.F_OK)
os.access('/path', os.X_OK)
os.access('/path', os.W_OK)
os.access('/path', os.R_OK)


def is_readable(path, user):
    user_info = pwd.getpwnam(user)
    uid = user_info.pw_uid
    gid = user_info.pw_gid
    s = os.stat(path)
    mode = s[stat.ST_MODE]
    return (
        ((s[stat.ST_UID] == uid) and (mode & stat.S_IRUSR > 0)) or
        ((s[stat.ST_GID] == gid) and (mode & stat.S_IRGRP > 0)) or
        (mode & stat.S_IROTH > 0)
     )

def is_writable(path, user):
    user_info = pwd.getpwnam(user)
    uid = user_info.pw_uid
    gid = user_info.pw_gid
    s = os.stat(path)
    mode = s[stat.ST_MODE]
    return (
        ((s[stat.ST_UID] == uid) and (mode & stat.S_IWUSR > 0)) or
        ((s[stat.ST_GID] == gid) and (mode & stat.S_IWGRP > 0)) or
        (mode & stat.S_IWOTH > 0)
     )

def is_executable(path, user):
    user_info = pwd.getpwnam(user)
    uid = user_info.pw_uid
    gid = user_info.pw_gid
    s = os.stat(path)
    mode = s[stat.ST_MODE]
    return (
        ((s[stat.ST_UID] == uid) and (mode & stat.S_IXUSR > 0)) or
        ((s[stat.ST_GID] == gid) and (mode & stat.S_IXGRP > 0)) or
        (mode & stat.S_IXOTH > 0)
     )


if __name__ == '__main__':
    print is_writable('/opt', getpass.getuser())
