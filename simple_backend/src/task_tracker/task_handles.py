from fastapi.routing import APIRouter
from Shemas_task import Status

route=APIRouter()

j={}

@route.get("/tasks")
def get_tasks():
    return j

@route.post("/tasks")
def create_task(task):
    j[len(j)+1]={"task":task,"status":Status.unactive}
    return j

@route.put("/tasks/{task_id}")
def update_task(task_id: int, new_task:str=None,status:Status=None):
    if task_id in j:
        if new_task is not None:
            j[task_id]["task"] = new_task
        if status is not None:
            j[task_id]["status"]=status
    return j

@route.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    j.pop(task_id)
    return j
