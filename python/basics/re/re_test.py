# -*- coding: utf-8 -*-
import re
import uuid


s = 'speed=210, angle=150'
m = re.findall(r'(\w*[0-9]+)\w*', s)
print m

s = '103.1234?\r\n'
m = re.findall(r'-?\d+\.?\d+', s)
print m

pattern = re.compile(r'-?\d+\.?\d+')
match = pattern.search('103.1234?\r\n')
if match:
    print match.group()


# 替换所有匹配的子串
# re.sub(pattern, repl, string, count=0, flags=0)  # 只返回替换后的字符串
# re.subn(pattern, repl, string, count=0, flags=0)  # 返回一个元组, (替换后的字符串, 被替换的数量)

s = 'jquery-1.12.3-(kdfj-123\中文)(%s).zip' % str(uuid.uuid4())

print re.subn(r'\(\S+?\)', '', s)

pattern = re.compile(r'\(\S+?\)')
print pattern.subn('', s)


# 替换邮箱prefix
def encrypt_email(mail, repl='####', pattern=re.compile(r'^([a-z0-9_\.-]+)(?=@)')):
    """
    脱敏邮箱地址
    eg: john@gmail.com => ####@gmail.com
    """
    return pattern.sub(repl, mail)


print re.findall(r'\(\S+?\)', s)  # 匹配括号结果中包含括号

print re.findall(r'(?<=\()\S+?(?=\))', s)   # 匹配括号结果中不包含括号

uuid_val = re.findall(r'(?<=\()\S+?(?=\))', s)[-1]
print s.replace(uuid_val, '')
uuid_val = re.findall(r'\(\S+?\)', s)[-1]


# re.split(pattern, string, maxsplit=0)  maxsplit是分离的次数, maxsplit=1分离一次, 默认为0

# reresult = re.split(regex, subject)

# rereobj = re.compile(regex)
# result = reobj.split(subject)匹配
