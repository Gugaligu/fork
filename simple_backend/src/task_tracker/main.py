import uvicorn
from fastapi import FastAPI

app = FastAPI()

j={}

@app.get("/tasks")
def get_tasks():
    return j

@app.post("/tasks")
def create_task(task):
    j[len(j)+1]=task
    return j

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_data):
    j[task_id]=new_data
    return j

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    j.pop(task_id)
    return j

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)