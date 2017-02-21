#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika


# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

connection = pika.BlockingConnection(
    # pika.URLParameters('amqp://baixue:baixue@localhost:5672/test_vhost')
    pika.URLParameters('amqp://dts3:yuhjnm@192.168.162.108:5672/dtsvhost')
)

channel = connection.channel()

channel.queue_declare(queue='hello')


channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
