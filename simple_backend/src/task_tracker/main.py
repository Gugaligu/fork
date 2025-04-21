from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()

j={}
class Status(Enum):
    active = "active"
    unactive = "unactive"
    completed = "completed"

@app.get("/tasks")
def get_tasks():
    return j

@app.post("/tasks")
def create_task(task):
    j[len(j)+1]={"task":task,"status":Status.unactive}
    return j

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task:str=None,status:Status=None):
    if new_task is None:
        j[task_id]["task"] = new_task
    if status is None:
        j[task_id]["status"]=status
    return j

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    j.pop(task_id)
    return j

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)