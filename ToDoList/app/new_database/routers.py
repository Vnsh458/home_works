from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert, update, delete
from models import TaskModel
from schemas import TaskCreateS, TaskUpdateS


task_router = APIRouter(prefix='/api/v1/tasks')

@task_router.get(path='/list/')
def tasks_list_point(request: Request):
	session = Session(engine)
	stmt = select(TaskModel)
	request_db = session.execute(stmt)
	tasks:list = request_db.scalars().all()
	session.close()
	return tasks

@task_router.post(path='/create/')
def create_task_point(request: Request, task: TaskCreateS):
	session = Session(engine)
	stmt = insert(TaskModel).values(
		title=task.title,
		description=task.description,
		deadline=task.deadline
	)
	session.execute(stmt)
	session.commit()
	session.close()
	return task

@task_router.put(path='/update/')
def update_task_point(request: Request, task_id: int, new_task: TaskUpdateS):
	session = Session(engine)
	stmt = update(TaskModel).where(TaskModel.id == task_id).values(
		title=new_task.title,
		description=new_task.description,
		status=new_task.status,
		deadline=new_task.deadline
	)
	session.execute(stmt)
	session.commit()
	session.close()
	return new_task

@task_router.delete(path='/delete/{task_id}/')
def delete_task_point(request: Request, task_id: int):
	session = Session(engine)
	stmt = delete(TaskModel).where(TaskModel.id == task_id)
	session.execute(stmt)
	session.commit()
	session.close()
	return "Task deleted"