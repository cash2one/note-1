#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Django Http请求、响应和中间件'''

__author__ = 'baixue'

'''HttpRequest'''

'''
HttpRequest 最常用的两个属性 GET和POST
它们的数据结构和Python内置的dict很像，不过它们是Django内置的dict子类QueryDict的实例, 
它的"键--值"里的值都是list
'''
'''
GET参数是作为URL字符串的一部分传递进来的，但是并不属于URL本身
'''
# 通过GET变量告诉服务器所需的页码
'/userlist/?page=2'

def userlist(request):
	return paginated_userlist_page(page=request.GET['page'])

'''
POST参数不属于URL的一部分，所以用户是看不到的, 通常它们是web页面上由HTML表单生成的。
FORM标签的action参数指明了数据要提交给哪一个URL， 用户提交表单的时候，URL就会随着由
表单字段组成的POST字典一起调用
'''

'''
除了GET和POST，HttpRequest还有一个REQUEST字典，它会搜索前面两个字典视图返回一个被请求的键
'''


'''
Cookies和Sessions
'''
'''
request.Cookies 也是一个字典，代表了存储在请求里的HTTP cookies。
cookies是网页里一种在用户浏览器里存储持久化信息的手段

大多数cookies都是用来支持一个叫做会话的特性，这代表一个网页可以向浏览器要求一个能
标识用户的值（这个信息可以在用户首次连接网站或登录的时候设置），然后用这个信息来为用户
提供定制行为的页面

cookies在客户端可以被随意的更改，所以存放关键数据是不安全的

Sessions通常用来实现状态，也是个字典类型

其他属性：
path
method
encoding
FILES
META
user
raw_post_data
'''


'''Response'''

'''
响应比请求简单，其主要数据就是存放在content属性里的正文(body text)

response = HttpResponse('')
response.write("<html>")
response.write("This is a tiny Web page!')
response.write("</html>")

设置http头
response = HttpResponse()
response["Content-Type"] = "text/csv"
response["Content-Lengthn"] = 256

Django为很多常见的响应类型提供了HttpResponse子类
HttpResponseForbidden(即HTTP 403)
HttpResponseServerError(即HTTP 500----服务器内部错误)
'''


'''中间件'''
'''
在settings.py文件里的MIDDLEWARE_CLASSES元组里列出后，Django会内省这些类
，并在适当的时候调用其方法。
类在设置文件里罗列的顺序决定了它们执行的顺序
'''

'''Django自带了很多内置的中间件'''

'''请求中间件'''
'''一般用在输入端，它定义为一个实现了process_request方法的类'''
from some_exterior_auth_lib import get_user

	class ExteriorAuthMiddleware(object):
		def process_request(self, request):
			token = request.COOKIES.get('auth-token')
			if token is None and not request.path.startswith('/login'):
				return HttpResponseRedirect ('/login/')
			# 给请求对象添加了额外属性
			request.exterior_user = get_user(token)

'''响应中间件'''

'''
响应中间件是运行在视图函数返回的HttpResponse对象之上，这样的中间件
必须实现process_reponse方法，这个方法接受一个Request和一个Response参数
并返回一个HttpResponse或子类的对象。

响应中间件最常见的用法就是在响应里插入额外的头信息
'''
# 例子
class TextFilterMiddleware(object):
	def process_response(self, request, response):
		response.content = response.content.replace ('foo', 'bar')



'''视图'''

'''通用视图'''

'''半通用视图'''

'''自定义视图'''
'''
django.shortcuts模块----提供捷径
render-to-response
Http404
get_object_or_404
get_list_or_404
'''
















