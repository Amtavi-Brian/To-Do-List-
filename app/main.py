from fastapi import FastAPI

from app.database import engine, Base
from app.routers import todos
import app.models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo API",
    version="1.0.0"
)


app.include_router(todos.router)


@app.get("/")
def home():
    return {
        "message": "Todo API is running"
    }