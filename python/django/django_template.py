#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''django模板'''

__author__ = 'baixue'

'''
模板系统不只用来生成html，还可以用来生成log文件，E-mail正文，CSV文件等任何文本格式
'''

'''
使用哪个模板以及渲染什么数据是由视图函数本身(render_to_response)
或者视图的参数(比如通用视图的template_name参数)决定的
'''

'''
django里把一个传给渲染模板的信息称为context, 一个context基本就是一个包含键值对的dict
'''

'''
给context提供数据的方法，通用视图里context会为你事先准备好，只需要把extra_context参数附加上去就行了
另一种给模板context提供数据的方法就是通过context处理器，context处理器(和中间件一样)需要在settings.py里
用python模块语法引用才能激活(TEMPLATE_CONTEXT_PROCESSORS, 另外其执行顺序和中间件一样，是按设置顺序执行的)
'''


'''模板语言语法'''

'''
变量输出{{ variable }}
命令{{ command }}
'''
# 例
# context
({"title_text" : "My Webpage", "object_list" : ["One", "Two", "Three"]})

<html>
	<head>
		<title>{{ title_text }}</title>
	</head>
	<body>
		<ul>
		{% for item in object_list %}
			<li>{{ item }}</item>
		{% endfor %}
		</ul>
	</body>
</html>

# 注意：当在模板里输出context变量的时候， 它会隐式的调用unicode方法
# 如果打印一个没有定义 __unicode__方法的对象，模板里什么也看不到


'''模板过滤器'''

'''
django提供了各式各样的过滤器来封装web开发中常见的文本处理工作
例如：转义斜杠符号、大写首字、格式化日期、获取列表或元组的长度，以及连接字符串等
'''
# 转小写
<ul>
{% for string in string_list %}
 <li>{{ string | lower }}</li>
{% endfor %}
</ul>

# yesno过滤器可以接受任何值(一般是boolean)并打印出可读字符串
<table>
	<tr>
		<th>Name</th>
		<th>Available?</th>
	</tr>
	{% for person in person_list %}
	<tr>
		<td>{{ person.name }}
		<td>{{ person.is_availble | yesno:"Yes, no" }}</td>
	</tr>
	{% endor %}
</table>


'''标签'''
# 逻辑操作
{% if %}
{% ifequal %}
# 模板包含/继承
{% block %}
{% include %}
{% extends %}

# 迭代列表的内容前检查它的长度
{% ifequal object_list | length 10 %}
	<ul>
	{% for item in object_list %}
		<li>{{ item }}</li>
	{% endfor %}
	</ul>
{% endifequal %}

# length_is过滤器
{% if object_list | length_is:10 %}
	<ul>
	{% for item in object_list %}
		<li>{{ item }}</li>
	{% endfor %}
	</ul>
{% endifequal %}


# 模板继承
<html>
	<head>
		<title>{% block title %}My Web site{% endblock %}</title>
	</head>
	<body>
		<div id-"header">
			<a href="/sectionl/">Section l</a>
			<a href="/section2/">Section 2</a>
		</div>
		<div id="content">
			(% block content %}{% endblock %}
		</div>
		<div id="footer">
			<a href="/about/">About The Site</a>
		</div>
	</body>
</html>

# section1.html
{% extends "base.html" %}
{% block title %}Section 1{% endblock %}

# section2.html
{% extends "base.html" %}
{% block title %}Section 2{% endblock %}

# page1.html
{% extends "section1.html" %}
{% block content %}this is page 1{% endblock %}

# page2.html
{% extends "section2.html" %}
{% block content %}this is page 2{% endblock %}




























