# -*- coding: utf-8 -*-

# environ：一个包含所有HTTP请求信息的dict对象
# start_response():一个发送HTTP响应的函数
# start_response()函数接收两个参数:
# 一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示.
# HTTP响应分为Header和Body两部分（Body是可选项）
# 200表示一个成功的响应，后面的OK是说明。失败的响应有404 Not Found：网页不存在，
# 500 Internal Server Error：服务器内部出错，等等
# Content-Type指示响应的内容，这里是text/html表示HTML网页。
# 请注意，浏览器就是依靠Content-Type来判断响应的内容是网页还是图片，是视频还是音乐.
# 浏览器并不靠URL来判断响应的内容，所以，即使URL是http://example.com/abc.jpg，它也不一定就是图片
# HTTP响应的Body就是HTML源码
# 当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，
# 然后，根据HTML里面的各种链接，再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，
# 最终显示出一个完整的页面.

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


def application2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
