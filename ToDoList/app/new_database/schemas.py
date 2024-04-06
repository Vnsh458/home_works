from pydantic import BaseModel


class TaskCreateS(BaseModel):
	title: str
	description: str
	deadline: str |None=None

class TaskUpdateS(TaskCreateS):
	status: bool