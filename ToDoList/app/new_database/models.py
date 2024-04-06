from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Boolean


class Model(DeclarativeBase):
	pass


class TaskModel(Model):
	__tablename__ = "tasks"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	description: Mapped[str]
	status: Mapped[bool] = mapped_column(Boolean, default=False)
	deadline: Mapped[str]
