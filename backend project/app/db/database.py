from sqlalchemy import create_engine
from db.config import database_url

engine = create_engine(database_url, echo=True)