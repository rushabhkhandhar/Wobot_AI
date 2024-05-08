# main.py

from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List, Optional
from authentication import get_current_user
from database import todos_collection
from models import TodoCreate, TodoUpdate
from fastapi import Depends

app = FastAPI()

security = HTTPBasic()
#test api :- http://localhost:8000/todos
@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate, credentials: HTTPBasicCredentials = Depends(security)):
    current_user = get_current_user(credentials)
    new_todo = {"title": todo.title, "description": todo.description, "user": current_user}
    result = todos_collection.insert_one(new_todo)
    return {"id": str(result.inserted_id), "title": new_todo["title"], "description": new_todo["description"]}

#test api :- http://localhost:8000/todos/{todo_id}
@app.get("/todos/{todo_id}")
def read_todo(todo_id: str, credentials: HTTPBasicCredentials = Depends(security)):
    current_user = get_current_user(credentials)
    todo = todos_collection.find_one({"_id": ObjectId(todo_id), "user": current_user})
    todo['_id'] = str(todo['_id'])
    if not todo:
        raise HTTPException(status_code=404, detail= f"Todo not found {current_user}, {type(todo)=}")
    return todo

#test api :- http://localhost:8000/todos
@app.get("/todos")
def read_todos(credentials: HTTPBasicCredentials = Depends(security)):
    current_user = get_current_user(credentials)
    todos = todos_collection.find({"user": current_user})
    todos_ = []
    for i in todos:
        i["_id"] = str(i["_id"])
        todos_.append(i)
    return {"TodoList" : todos_}

#test api :- http://localhost:8000/todos/{todo_id}
@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: TodoUpdate, credentials: HTTPBasicCredentials = Depends(security)):
    current_user = get_current_user(credentials)
    existing_todo = todos_collection.find_one({"_id": ObjectId(todo_id), "user": current_user})
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    update_values = {k: v for k, v in todo.dict().items() if v is not None}
    todos_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_values})
    return {"message": "Todo updated successfully"}

#test api :- http://localhost:8000/todos/{todo_id}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str, credentials: HTTPBasicCredentials = Depends(security)):
    current_user = get_current_user(credentials)
    result = todos_collection.delete_one({"_id": ObjectId(todo_id), "user": current_user})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
