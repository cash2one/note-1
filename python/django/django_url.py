#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''学习Django的url设置'''


from django.conf.urls.defaults import *


urlpatterns = patterns('myproject.myapp.views',
	# 定义首页
	(r'^$', 'index'),
	(r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive'),
)
# 如果某个url项要include其他URLconf文件的话，就不用在后面加"$"
# 如果patterns的第一个参数非空，它就会被加到函数字符串之间，例如上例
# 完整的python模块路径就是'myproject.myapp.views.index'和'myproject.myapp.views.archive'

# url方法接受三个参数(正则表达式， 视图字符串/函数, kwargs字典参数, name)
# name是个可选参数，它必须保持唯一，可以在其他地方通过它来应用URL
urlpatterns = patterns('myproject.myapp.views',
	url(r'^$', 'index', name='index'),
	url(r'^archives/(?P<year>\d(4))/(?P<month>\d(2))/(?P<day>\d(2))/$', 'archive', name='archive'),
)

# 使用多个patterns
urlpatterns = patterns('myproject.blog.views',
	url(r'^$', 'index'),
	url(r'^blog/new$', 'new_post'),
	url(r'^blog/topics/(?P<topic_name>\w+)/new/$', 'new_post'),
)

urlpatterns += patterns('myproject.guestbook.views',
	url(r'^guestbook$', 'index'),
	url(r'^guestbook/add/$', 'new_entry'),
)

urlpatterns += patterns('myproject.catalog.views',
	url(r'^catalog$', 'index'),
)

# 用include更新上例
# urls.py
urlpatterns = patterns('myproject.blog.views',
	url(r'^$', 'index'),
	url(r'^blog/', include('myproject.blog.urls'),
)

urlpatterns += patterns('',
	url (r'^guestbook/', include('myproject. guestbook.urls')) ,
)

urlpatterns += patterns('',
	url(r'^catalog/', include('myproject.catalog.urls')),
)

## blog/urls/py
urlpatterns = patterns('myproject.blog.views',
	url(r'^new/$', 'new_post'),
	url(r'^topics/(?P<topic_name>\w+)/new/$', 'new_post'),
)

## guestbook/urls.py
urpatterns += patterns('myproject.guestbook.views',
	url(r'^$', 'index'),
	url(r'^add/$', 'new_entry'),
)

## catalog/urls.py
urlpatterns += patterns('myproject.catalog.views',
	url(r'^$', 'index'),
)


'''
符号	            匹配
. (dot)	            任意单一字符
\d	                任意一位数字
[A-Z]	            A 到 Z中任意一个字符(大写)
[a-z]	            a 到 z中任意一个字符(小写)
[A-Za-z]	        a 到 z中任意一个字符(不区分大小写)
+					匹配一个或更多(例如, \d+ 匹配一个或 多个数字字符)
[^/]+				一个或多个不为‘/’的字符
?					零个或一个之前的表达式(例如：\d? 匹配零个或一个数字)
*					匹配0个或更多(例如, \d* 匹配0个 或更多数字字符)
{1,3}				介于一个和三个（包含）之前的表达式(例如，\d{1,3}匹配一个或两个或三个数字)
'''



