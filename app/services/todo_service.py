from sqlalchemy.orm import Session

from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate, TodoPatch


#Adding a new Todo
def create_todo(db: Session, todo: TodoCreate):

    new_todo = Todo(
        title=todo.title,
        completed=todo.completed
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
def get_todo(db: Session, todo_id: int):
    return (
        db.query(Todo).filter(Todo.id == todo_id).first()
    )
# Updating the Todo in the database
def update_todo(
        db: Session,
        todo_id: int,
        todo_update: TodoUpdate | TodoPatch
):
    existing_todo = get_todo(db, todo_id)

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
    todo: TodoPatch
):

    existing_todo = get_todo(db, todo_id)

    if existing_todo is None:
        return None

    update_data = todo.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(existing_todo, field, value)

    db.commit()
    db.refresh(existing_todo)

    return existing_todo
# Deleting the Todo from the database
def delete_todo(db: Session, todo_id: int):

    existing_todo = get_todo(db, todo_id)

    if existing_todo is None:
        return False

    db.delete(existing_todo)
    db.commit()

    return True