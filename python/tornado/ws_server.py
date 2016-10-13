#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.websocket
import tornado.ioloop


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"Welcome " + message)

    def on_close(self):
        print("WebSocket closed")


class StringHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request.full_url()
        self.write('Hello Golang')


def make_app():
    return tornado.web.Application([
        (r"/string", StringHandler),
        (r"/websocket", EchoWebSocket),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
