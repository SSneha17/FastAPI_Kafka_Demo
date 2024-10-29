# FastAPI_Kafka_Demo
A stock portfolio app that allows user to buy a stock and display the portfolio snapshot. When the stock is purchased, the API emits the updated balance informatio to Kafka. The Kafka consumer will read the data and in turn updtae the total portfolio balance.
The angular UI shows the updated balance in real time by using websocket service that consumes the Kafka broker.

Tech Stack-
  -Backend: Python FastAPI, Kafka, and Web Socket
  -Frontend: Angular 17 and websocket service
