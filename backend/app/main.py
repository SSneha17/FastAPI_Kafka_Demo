from fastapi import FastAPI, BackgroundTasks, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from user_service import user
from stock_service import stock
from kafka_consumer import consume_kafka_topic
from kafka import KafkaConsumer
import json
import asyncio



app= FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.allow_origins =["*"]
app.include_router(user)
app.include_router(stock)


'''
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume_kafka_topic("stock-details", "localhost:29092"))
'''

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        print("hello")
        balance = await consume_kafka_topic("stock-details", "localhost:29092")   
        print(balance)
        await websocket.send_json(balance)
        #await asyncio.sleep(1)  # Adjust the sleep interval as needed

