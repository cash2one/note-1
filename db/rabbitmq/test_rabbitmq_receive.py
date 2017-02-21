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


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
