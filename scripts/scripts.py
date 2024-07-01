from handlers.postgres import get_engine
from sqlalchemy import text


def create_tables():
    engine = get_engine()
    with engine.connect() as con:
        with open("data\data.sql") as file:
            query = text(file.read())
            con.execute(query)