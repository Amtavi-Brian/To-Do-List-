from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a Todo API", "completed": False},
]


class Todo(BaseModel):
    title: str
    completed: bool = False


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": todo.completed
    }

    todos.append(new_todo)

    return new_todo