from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from routers import tasks_list_point, create_task_point


task_template = APIRouter()
templates = Jinja2Templates(directory='templates')

@task_template.get('/')
def show_homepage(request: Request):
	tasks:dict = {"tasks": tasks_list_point(request)}
	return templates.TemplateResponse(request=request, name='home_page.html', context=tasks)

@task_template.get('/about')
def show_aboutpage(request: Request):
	return templates.TemplateResponse(request=request, name='about_page.html')

@task_template.get('/autorisation')
def show_autorisation(request: Request):
	return templates.TemplateResponse(request=request, name='auto_page.html')
