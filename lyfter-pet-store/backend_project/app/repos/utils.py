from sqlalchemy import select

#opens the connection to avoid creating this in every method
def with_connection(method):
  def wrapper(self, *args, **kwargs):
    with self.engine.connect() as conn:
      return method(self, conn, *args, **kwargs)
  return wrapper