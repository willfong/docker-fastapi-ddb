import uuid
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from ..services import todo, util

router = APIRouter()

class TodoNew(BaseModel):
    name: str

@router.get("/")
def todo_root():
    return {"msg": "Hello, World!"}

@router.post("/add")
def todo_add(newtodo: TodoNew):
    id = str(uuid.uuid4())
    dt = datetime.utcnow().isoformat()
    if todo.add(id, dt, 'haha', newtodo.name):
        return {"msg": "success"}
    return {"msg": "error inserting todo task"}
