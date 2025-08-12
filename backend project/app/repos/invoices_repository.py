from sqlalchemy import select, Select
from sqlalchemy.engine import CursorResult
from db.models import invoices_table
from repos.utils import with_connection


class InvoicesRepository:
  def __init__(self, engine):
    self.engine = engine

  @with_connection
  def get_invoices(self, conn, stmt : Select) -> CursorResult:
    return conn.execute(stmt)


  @with_connection
  def get_user_invoices(self, conn, user_id : int):
    stmt = conn.execute(select(invoices_table).where(
        (invoices_table.c.user_id == user_id)
    )).fetchall()

    if not stmt:
      return None

    invoices = [dict(row._mapping) for row in stmt]

    return invoices