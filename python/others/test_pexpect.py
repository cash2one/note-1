#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pexpect


child = pexpect.spawn('redis-cli')
i = child.expect(['127.0.0.1:6379>', pexpect.EOF, pexpect.TIMEOUT], timeout=10)
print i
if i == 0:
    print 'success'
else:
    print 'fail'

child.sendline('set baixue 4')
i = child.expect(['127.0.0.1:6379>', pexpect.EOF, pexpect.TIMEOUT], timeout=10)
print i
if i == 0:
    print 'before:'
    print child.before
    print 'success'
else:
    print 'fail'

child.sendeof()
child.close()
