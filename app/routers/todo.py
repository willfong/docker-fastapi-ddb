import uuid
from fastapi import APIRouter, Header
from pydantic import BaseModel
from datetime import datetime
from ..services import todo, util

router = APIRouter()

class TodoNew(BaseModel):
    name: str

@router.get("/")
def todo_root(*, authorization: str = Header(None)):
    util.logger.warning(f"todo_root: Authorization Header: {authorization}")
    user_data = util.get_user_data_from_token(authorization)
    return {"msg": user_data}

@router.post("/add")
def todo_add(newtodo: TodoNew, authorization: str = Header(None)):
    util.logger.warning(f"Authorization Header: {authorization}")
    user_id = util.get_user_data_from_token(authorization).get('sub')
    util.logger.warning(f"User ID: {user_id}")
    id = str(uuid.uuid4())
    dt = datetime.utcnow().isoformat()
    if todo.add(id, dt, user_id, newtodo.name):
        return {"msg": "success"}
    return {"msg": "error inserting todo task"}
