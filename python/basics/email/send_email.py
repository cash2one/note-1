#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''发送邮件测试'''

__author__ = 'baixue'

import smtplib
from email.mime.text import MIMEText


mailto_list = ["baixuexue123@hotmail.com"]
mail_host = "smtp.sina.com"
mail_user = "baixuexue123@sina.com"
mail_pass = "xuebailove321"
mail_postfix = "sina.com"

content = "python email test!"
msg = MIMEText(content, _charset='gbk')
msg['Subject'] = "python email test!"
msg['From'] = "baixuexue123@sina.com"
msg['To'] = ";".join(mailto_list)

server = smtplib.SMTP()
server.connect(mail_host)
server.login(mail_user, mail_pass)
server.sendmail(mail_user, mailto_list, msg.as_string())
server.close()



if __name__ == "__main__":
    pass
