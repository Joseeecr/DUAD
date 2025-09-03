from sqlalchemy import create_engine

class DbConnection:
  def __init__(self):
    self.engine = create_engine("postgresql://postgres:54321@localhost:5432/postgres", echo = True)