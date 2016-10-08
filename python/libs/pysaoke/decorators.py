# -*- coding: utf-8 -*-

""" decorator """

import time
import traceback
import functools
import threading import Thread


def clock(ms=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            st, st_c = time.time(), time.clock()
            ret = func(*args, **kwargs)
            print 'run time: %.1fms' % ((time.time()-st)*1000) if ms else 'run time: %.4fs' % (time.time()-st)
            print 'cpu time: %.1fms' % ((time.clock()-st_c)*1000) if ms else 'cpu time: %.4fs' % (time.clock()-st_c)
            return ret
        return wrapper
    return decorator


def catch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print '>>>>>>>>' + wrapper.__name__ + '>>>>>>>>'
            traceback.print_exc()
    return wrapper


def trace_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print '>>>>>>>> function *%s* is called :: %s >>>>>>>>' % \
              (wrapper.__name__, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return func(*args, **kwargs)
    return wrapper


def async(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
