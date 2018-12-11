# -*- coding: utf-8 -*-


import pika
import os
import argparse


parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-r", "--receive", action = 'store_true', help ='set this option to switch to receive mode' )
parser.add_argument("-s", "--sendmany",type=int,default=1)
args = parser.parse_args()

import amqpkey
amqp_url = amqpkey.key

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 20

connection = pika.BlockingConnection(params)
channel= connection.channel()
channel.queue_declare(queue='hello2')

if not args.receive: 
    for i in range(args.sendmany):
        msg=channel.basic_publish(exchange='', routing_key='hello2', body='Hello')
        print("Send")
    connection.close()
        
else:
    cpt = 0
    def callback(ch,method,properties,body):
        print("Reçu");
        global cpt 
        cpt += 1;
        print(cpt)
    channel.basic_consume(callback,queue='hello2',no_ack=True) 
    print("Waiting for message. To exit press CTRL+C")
    channel.start_consuming()