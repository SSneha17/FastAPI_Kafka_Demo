import json
import asyncio
from aiokafka import AIOKafkaConsumer
from user_service import users, update_balance
from stock_service import update_stock
from model import Stock
import json


async def consume_kafka_topic(topic_name, bootstrap_servers):
    consumer = AIOKafkaConsumer(
        topic_name,
        bootstrap_servers=bootstrap_servers
        #group_id="kafka-fastapi"  # Choose a suitable group ID
    )
    await consumer.start()

    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode('utf-8'))
            s: Stock = data
            print(f"Received message: {s}")
            balance = await update_balance(s)
            print("stock data updated")
            return balance
            

    finally:
        await consumer.stop()



#if __name__ == "__main__":
#    asyncio.run(consume_kafka_topic("stock-details", "localhost:29092"))