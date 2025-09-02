from sqlalchemy import select

#opens the connection to avoid creating this in every method
def with_connection(method):
  def wrapper(self, *args, **kwargs):
    with self.engine.connect() as conn:
      return method(self, conn, *args, **kwargs)
  return wrapper


def validate_column_and_query_value(conn, table, column : str , value : str | int) -> bool:

  if not hasattr(table.c, column):
    raise ValueError(f"Column '{column}' does not exist in table.")

  column_attr = getattr(table.c, column)
  stmt = select(table).where(column_attr == value)
  result = conn.execute(stmt).first()

  return result is not None


def apply_filters(stmt, table, filters: dict, conn, allowed_fields: list):
  for field in allowed_fields:
    if field in filters:
      value = filters[field]
      if validate_column_and_query_value(conn, table, field, value):
        stmt = stmt.where(getattr(table.c, field) == value)
      else:
        raise ValueError(f"No record found")
    return stmt


