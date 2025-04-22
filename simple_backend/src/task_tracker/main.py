
import uvicorn
from fastapi import FastAPI
from task_handles import route as task

app = FastAPI()
app.include_router(task)




if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)

