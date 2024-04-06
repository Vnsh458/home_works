from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from database import engine
from models import TaskModel
from routers import task_router
from urls import task_template


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(task_router)
app.include_router(task_template)

if __name__ == "__main__":
	TaskModel.metadata.create_all(engine)
	uvicorn.run('main:app', port=8000, reload=True)