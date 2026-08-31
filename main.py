from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Todo
from schemas import TodoCreate, TodoUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Todo API is running"}


@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):

    new_todo = Todo(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(
            status_code=404,
             detail="Todo not found")   
        # return {"error": "Todo not found"}
    return todo


@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if existing_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    existing_todo.title = todo.title
    existing_todo.completed = todo.completed
    db.commit()
    db.refresh(existing_todo)
    return existing_todo