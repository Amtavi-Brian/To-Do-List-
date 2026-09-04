from fastapi import FastAPI

from app.routers import todos
from app.auth.router import router as auth_router


app = FastAPI(
    title="Todo API",
    version="1.0.0"
)

app.include_router(todos.router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Todo API is running"}