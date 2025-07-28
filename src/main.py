from fastapi import FastAPI
from src.routers import orders

app = FastAPI()
app.include_router(orders.router)
