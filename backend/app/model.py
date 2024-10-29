from typing import List
from pydantic import BaseModel


class Stock(BaseModel):

    name: str
    quantity: int
    price: float
    class Config:
        schema = {
            "stock":{
            
        "name":"AAPL",
        "quantity":1,
        "price": 100.00
    }
        }

class ResponseData(BaseModel):
    stock: str
    quantity: int

class User(BaseModel):
    balance: float
    stocks : List[Stock]
    class Config:
        schema = {
            "user":{            
        "balance":100.00,
        "stocks": [
            {            
            "name":"AAPL",
            "quantity":1,
            "price": 100.00}
            ]}
    }
        
