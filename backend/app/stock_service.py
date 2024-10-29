from fastapi import APIRouter
from model import Stock, ResponseData
#from kafka_producer import send_data, producer
import json
from kafka import KafkaProducer
from typing import List
import user_service

ORDER_KAFKA_TOPIC = "stock-details"
producer = KafkaProducer(bootstrap_servers='localhost:29092')

stocks = [
    {    
        "name":"AAPL",
        "quantity":1,
        "price":200.00
    },
    {
             
        "name":"NVDA",
        "quantity":1,
        "price": 120.00
    },
    {
       
        "name":"TSLA",
        "quantity":1,
        "price": 200.00
    },
    
]


stock= APIRouter()


@stock.get("/stocks", tags=["stocks"])
async def get_stocks():
    return {"data": stocks}

@stock.get("/stocks/{name}", tags=["stocks"])
async def get_stock_by_Name(name: str):

    for s in stocks: 
               
        print(s)
        if s["name"] == name:
            return {"data": s}
    return {"error":"stock not found!"}

def update_stock(data: Stock):
    for u in stocks:
        if u["name"] == data.name:
            price = u["price"]
            #q = u["quantity"] 
            u["quantity"] += data.quantity
            u["price"] = (u["price"] + data.price)/ u["quantity"]            
            print (f"UPdated data: {u}")
            s= {"name":data.name, "quantity":data.quantity, "price": data.price}
            producer.send(ORDER_KAFKA_TOPIC, json.dumps(s).encode('utf-8'))
            return {"data":"Stock updated!"}    
    return {"error":"Stock not found!"}
 
'''
def update_stock(data: Stock):
    for u in stocks:
        if u["name"] == data["name"]:
            price = u["price"]
            #q = u["quantity"] 
            u["quantity"] += data["quantity"]
            u["price"] = (u["price"] + data["price"])/ u["quantity"]            
            print (u)
            data: Stock = {"name":u["name"], "quantity":u["quantity"], "price": u["price"]}
            producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode('utf-8'))
            return {"data":"Stock updated!"}    
    return {"error":"Stock not found!"}


'''

@stock.post("/buy_stock",tags=["stocks"])
async def add_stock(s: Stock):
    bal= user_service.check_balance()
    if float(bal) < float(s.price * s.quantity):
        return {"error":"Insufficient balance!"}
    for t in stocks:
        if s.name == t["name"]:
            print("updating..")
            return update_stock(s) 
    
    stocks.append(s.dict())
    
        #data : ResponseData= {"name": s.name, "quantity": s.quantity }
        #send_data(data)
    data = {"name":s.name, "quantity":s.quantity, "price": s.price}
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode('utf-8'))
        #kafka_producer.send_data(data)
    print(s)
    return {"data":"Stock Purchased!"}

