from sqlalchemy import Column, Integer, String

from database import Base, engine
from orm import create_tables


class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    surname = Column(String, nullable=False)


create_tables()
