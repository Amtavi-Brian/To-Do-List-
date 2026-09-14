from sqlalchemy.orm import Session

from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate, TodoPatch


#Adding a new Todo
def create_todo(db: Session, todo: TodoCreate, user_id: int):

    new_todo = Todo(
        title=todo.title,
        completed=todo.completed,
        user_id=user_id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo
# Retrieving the Todo from the database
def get_all_todos(
        db: Session,
        completed: bool | None = None,
        skip: int = 0,
        limit: int = 10
):
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(
            Todo.completed == completed
        )

    return query.offset(skip).limit(limit).all()

# Retrieving specific Todo from the database
def get_todo(
    db: Session,
    todo_id: int,
    user_id: int
):
    return (
        db.query(Todo)
        .filter(
            Todo.id == todo_id,
            Todo.user_id == user_id
        )
        .first()
    )
# Updating the Todo in the database
def update_todo(
        db: Session,
        todo_id: int,
        todo_update: TodoUpdate | TodoPatch,
        user_id: int
):
    existing_todo = get_todo(db, todo_id, user_id)

    if existing_todo is None:
        return None

    existing_todo.title = todo_update.title
    existing_todo.completed = todo_update.completed
    db.commit()
    db.refresh(existing_todo)

    return existing_todo
#Updating the Todo in the database using PATCH method
def patch_todo(
    db: Session,
    todo_id: int,
    todo: TodoPatch,
    user_id: int
):
    existing_todo = (
        db.query(Todo)
        .filter(
            Todo.id == todo_id,
            Todo.user_id == user_id
        )
        .first()
    )

    if existing_todo is None:
        return None

    if todo.title is not None:
        existing_todo.title = todo.title

    if todo.completed is not None:
        existing_todo.completed = todo.completed

    db.commit()
    db.refresh(existing_todo)

    return existing_todo
# Deleting the Todo from the database
def delete_todo(
    db: Session,
    todo_id: int,
    user_id: int
):
    existing_todo = (
        db.query(Todo)
        .filter(
            Todo.id == todo_id,
            Todo.user_id == user_id
        )
        .first()
    )

    if existing_todo is None:
        return None

    db.delete(existing_todo)
    db.commit()

    return existing_todo