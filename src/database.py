from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.DATABASE_URL_psycopg)
