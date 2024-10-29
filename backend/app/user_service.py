from fastapi import APIRouter
from model import Stock
from model import ResponseData
from kafka import KafkaConsumer
from stock_service import stocks


ORDER_KAFKA_TOPIC = "stock-details"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC, bootstrap_servers="localhost:29092"
)


'''
users = [
    {
        #"id": 1,
        "stock":"AAPL",
        "quantity": 3
    },
    {
        #"id": 2,
        "stock":"TSLA",
        "quantity": 1
    },
    {
       # "id": 3,
        "stock":"NVDA",
        "quantity": 1
    },
    
]
'''

users={

    "balance": 1000,
    "stocks": stocks
}

user= APIRouter()


@user.get("/users", tags=["user"])
async def get_users():
    #users.stocks = stocks    
    return {"data": users}


async def update_balance(data):
    print("Inside update_balance")
    print(f"Data : {data}")
    print(f"Initial Balance: {users['balance']}")
    users["balance"]-= (data["price"] * data["quantity"])
    print(f"Balance: {users['balance']}")
    return users["balance"]

def check_balance():
    return users["balance"]

'''

def update_stock(data: Stock):
    for u in users:
        if u["stock"] == data["stock"]:
            price = u["price"]
            #q = u["quantity"] 
            u["quantity"] += data["quantity"]
            u["price"] = (u["price"] + data["price"])/ u["quantity"]            
            print (u)
        else:
            {"error":"User not found!"}

'''