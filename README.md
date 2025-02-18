# Stock Portfolio App with Real-Time Updates Using Kafka

This is a **Stock Portfolio** app designed to demonstrate real-time streaming using **Kafka**. The app allows users to buy stocks, and the system will automatically update the portfolio balance in real-time using **Kafka producers** and **consumers**. Initially, the updated balance was only visible through the backend API (Swagger), but with the integration of **WebSockets**, the balance now updates live on the **UI**.

## Project Overview

The Stock Portfolio app consists of a backend built with **Python FastAPI** and a frontend built with **Angular17**. The app enables user to buy stocks against a predefined balance. When a user buys stocks, the backend calculates the updated balance and pushes the data to the **Kafka server** using a producer. The Kafka consumer then reads this message and updates the portfolio balance in real-time.

### Key Features:
- **Real-time portfolio balance updates** using **Kafka** and **WebSockets**.
- **Buy stocks** feature that updates the portfolio balance based on transactions.
- **Swagger API** to view and test backend functionality.
- Real-time UI updates reflecting changes in the portfolio balance.

## Tech Stack

- **Backend**: 
  - Python FastAPI
  - Kafka (for real-time streaming)
- **Frontend**: 
  - HTML, CSS, Typescript
  - WebSockets (for real-time updates)
- **Other**: 
  - Docker (for Kafka brokers and Zookeeper)
  - Swagger API for backend testing

## Project Setup

### Prerequisites

1. **Docker**: Ensure Docker is installed on your system to run the Kafka brokers and Zookeeper.
2. **Python**: Install Python (preferably version 3.7 or higher).
3. **Node.js**: Install Node.js for frontend dependencies (if required).

### Backend Setup (Python FastAPI)

1. Clone the repository:

   ```bash
   git clone https://github.com/SSneha17/FastAPI_Kafka_Demo.git
   cd backend
2. Install dependencies:

    ```bash
    .venv\Scripts\activate    #to enable the virtual environemnt
    pip install -r requirements.txt
3. Set up Kafka brokers and Zookeeper using Docker:

    ```bash
    docker-compose up -d
4.. Run the FastAPI server:

     
    cd app
    uvicorn app.main:app --reload

The backend should now be running at http://127.0.0.1:8000. To access the SWagger API, navigate to http://127.0.0.1:8000/docs

### Frontend Setup (Angular17)
1. Open the 'frontend' solution folder.
Install the frontend dependencies:

    ```bash
    npm install

2. Start the frontend server:

    ```bash
    ng serve -o

## In Action (Screenshots)
![image](https://github.com/user-attachments/assets/68d02ffb-d4e3-4418-83bc-a80bcd661205)

=>Purchasing new stock, SOFI (10 shares @15.00)

![image](https://github.com/user-attachments/assets/ac37a06b-598b-42d1-b931-5a4e1827bc27)

=> Adding 1 more share of existing stock, AAPL at 200

![image](https://github.com/user-attachments/assets/c85f7672-d39f-4714-90ea-19b9bf6b05c6)



