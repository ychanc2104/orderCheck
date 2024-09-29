import uvicorn
from fastapi import FastAPI

from dto import OrderDto
from services.CreateOrderService import CreateOrderService

app = FastAPI()


@app.post("/api/orders")
async def create_order(input: OrderDto):
    return CreateOrderService().request(input)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")