from sqlalchemy import create_engine, text

from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))

    print(f"{res.all()=}")
