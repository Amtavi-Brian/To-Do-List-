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
from app.services import todo_service
from app.auth.security import get_current_user
from app.models import User


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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return todo_service.create_todo(db, todo, current_user.id)


@router.get(
    "/",
    response_model=list[TodoResponse]
)
def get_todos(
    completed: bool | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return todo_service.get_all_todos(
        db,
        completed,
        skip,
        limit
    )


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = todo_service.get_todo(
        db,
        todo_id,
        current_user.id
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    updated_todo = todo_service.update_todo(
        db,
        todo_id,
        todo,
        current_user.id
    )

    if updated_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return updated_todo


@router.patch("/{todo_id}", response_model=TodoResponse)
def patch_todo(
    todo_id: int,
    todo: TodoPatch,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_todo = todo_service.patch_todo(
        db,
        todo_id,
        todo,
        current_user.id
    )

    if updated_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return updated_todo



@router.delete("/{todo_id}", response_model=TodoResponse)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted_todo = todo_service.delete_todo(
        db,
        todo_id,
        current_user.id
    )

    if deleted_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return deleted_todo