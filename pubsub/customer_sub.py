import pika
import json
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange = 'delivery', exchange_type='topic')
channel.queue_declare(queue='customer_updates')
channel.queue_bind(exchange = 'delivery', queue = 'customer_updates', routing_key = 'driver.location.1')

print('Waiting for logs.')

def callback(ch, method, properties, body):
    print(f"{body}")

channel.basic_consume(queue='customer_updates', on_message_callback=callback, auto_ack=True)

channel.start_consuming()