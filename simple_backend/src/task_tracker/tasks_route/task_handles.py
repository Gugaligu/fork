from fastapi.routing import APIRouter
from logic import TasksCRUD

from tasks_route.Shemas_task import Status, TaskCreate, TaskUpdate

route=APIRouter()


@route.get("/tasks")
def get_tasks():
    all_task = TasksCRUD.get_tasks()
    return all_task

@route.post("/tasks")
def create_task(task:TaskCreate):
    all_tasks = TasksCRUD.create_new_task(task.task,Status.unactive.value)
    return all_tasks

@route.put("/tasks/{task_id}")
def update_task(task_id: int, task:TaskUpdate):
    all_tasks=TasksCRUD.update_task(task_id,task.new_task,task.new_status)
    return all_tasks

@route.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    all_tasks=TasksCRUD.delete_task(task_id)
    return all_tasks
# обновить онлайн репозиторий
