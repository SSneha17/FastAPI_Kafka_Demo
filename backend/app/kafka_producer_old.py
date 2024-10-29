import json, time
from kafka import KafkaProducer, producer

ORDER_KAFKA_TOPIC = "stock_details"


producer = KafkaProducer(bootstrap_servers="localhost:29092")

def send_data(post_data):
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(post_data).encode('utf-8'))


