from fastapi.routing import APIRouter
from logic import TaskCloud, TasksCRUD

from tasks_route.Shemas_task import Status, TaskCreate, TaskModel

route=APIRouter(prefix="/tasks")


@route.get("")
def get_tasks():
    all_task = TasksCRUD.get()
    return all_task

@route.post("")
def create_task(task:TaskCreate):
    all_tasks = TasksCRUD.create(TaskModel(task=task.task,status=Status.unactive.value))
    return all_tasks

@route.put("/{task_id}")
def update_task(task_id: int, task:TaskModel):
    all_tasks=TasksCRUD.update(task_id,task)
    return all_tasks

@route.delete("/{task_id}")
def delete_task(task_id: int):
    all_tasks=TasksCRUD.delete(task_id)
    return all_tasks

@route.post("/local/sync")
def local_task_synk():
    all_tasks=TaskCloud.local_sync()
    return all_tasks

@route.post("/cloud/sync")
def cloud_task_synk():
    all_tasks=TaskCloud.cloud_sync()
    return all_tasks
