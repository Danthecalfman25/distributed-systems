import pika
import time
import json
import random

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange = 'delivery', exchange_type='topic')
    channel.queue_declare(queue='customer_updates')
    channel.basic_publish(exchange='delivery', routing_key='driver.location.1', body = 'location:')
    print("Sent Location")
    connection.close()


main()
        
    
