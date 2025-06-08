from sqlalchemy import select

#opens the connection to avoid creating this in every method
def with_connection(method):
  def wrapper(self, *args, **kwargs):
    with self.engine.connect() as conn:
      return method(self, conn, *args, **kwargs)
  return wrapper


def is_valid_id(conn, table, _id : int ) -> bool:
  stmt = select(table).where(table.c.id == _id)
  result = conn.execute(stmt).first()

  if not result:
    print("Id doesn't exists")
    return False
  return True