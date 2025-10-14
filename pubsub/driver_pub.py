import pika
import time
import json
import random

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='location')
    channel.basic_publish(exchange='', routing_key='location', body = 'location:')
    print("Sent Location")
    connection.close()


main()
        
    
