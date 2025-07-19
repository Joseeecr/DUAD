from sqlalchemy import create_engine
from config import database_url

engine = create_engine(database_url, echo=True)