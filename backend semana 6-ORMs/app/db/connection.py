from sqlalchemy import create_engine, MetaData

DB_URI = 'postgresql://postgres:54321@localhost:5432/postgres'

engine = create_engine(DB_URI, echo=True)
metadata_obj = MetaData(schema="orms_practice")