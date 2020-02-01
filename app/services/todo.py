from ..db import aws
from ..services import util

def add(pid, dt, uid, todo):
    if aws.ddb_todos_add_todo(pid, dt, uid, todo):
        return True
    return False

def get():
    return aws.ddb_todos_get_all()
