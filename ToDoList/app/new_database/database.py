from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker


DATABSE = "sqlite:///./db.db"
engine = create_engine(DATABSE, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()