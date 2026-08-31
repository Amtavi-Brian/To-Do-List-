from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Todo
from app.schemas import (
    TodoCreate,
    TodoUpdate,
    TodoPatch,
    TodoResponse
)


router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.post(
    "/",
    response_model=TodoResponse,
    status_code=201
)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):

    new_todo = Todo(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@router.get(
    "/",
    response_model=list[TodoResponse]
)
def get_todos(
    completed: bool | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    todos = query.offset(skip).limit(limit).all()

    return todos


@router.get(
    "/{todo_id}",
    response_model=TodoResponse
)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .first()
    )

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


@router.put(
    "/{todo_id}",
    response_model=TodoResponse
)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):

    existing_todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .first()
    )

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


@router.patch(
    "/{todo_id}",
    response_model=TodoResponse
)
def patch_todo(
    todo_id: int,
    todo: TodoPatch,
    db: Session = Depends(get_db)
):

    existing_todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .first()
    )

    if existing_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    update_data = todo.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(existing_todo, field, value)

    db.commit()
    db.refresh(existing_todo)

    return existing_todo


@router.delete(
    "/{todo_id}"
)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .first()
    )

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted successfully"
    }