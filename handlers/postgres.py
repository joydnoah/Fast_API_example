import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models.postgres.base import Base

load_dotenv()

def get_engine():
    database_uri = os.environ["DATABASE_URL"]
    database_uri = database_uri.replace("postgres://", "postgresql://")
    return create_engine(database_uri, echo=False)