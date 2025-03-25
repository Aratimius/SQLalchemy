from database import engine, Base


def create_tables():
    engine.echo = True
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

