from sqlalchemy import select
from db.tables import invoices_table
from repos.repos_utils import with_connection, validate_column_and_query_value
from typing import Optional
from exceptions.generated_exceptions import InvoiceNotFoundError

class InvoicesRepository:
  def __init__(self, engine, invoices_validator):
    self.engine = engine
    self.invoices_validator = invoices_validator

  @with_connection
  def get_invoices(self, conn, filters : dict) -> dict:
    stmt = select(invoices_table)

    if "id" in filters:
      if validate_column_and_query_value(conn, invoices_table, "id", filters["id"]):
        stmt = stmt.where(invoices_table.c.id == filters["id"])
      else:
        raise InvoiceNotFoundError(f"Invoice with id {filters["id"]} not found")

    if "user_id" in filters:
      if validate_column_and_query_value(conn, invoices_table, "user_id", filters["user_id"]):
        stmt = stmt.where(invoices_table.c.user_id == filters["user_id"])
      else:
        raise InvoiceNotFoundError(f"Invoice with user with id '{filters["user_id"]}' not found")
  
    if "shopping_cart_id" in filters:
      if validate_column_and_query_value(conn, invoices_table, "shopping_cart_id", filters["shopping_cart_id"]):
        stmt = stmt.where(invoices_table.c.shopping_cart_id == filters["shopping_cart_id"])
      else:
        raise InvoiceNotFoundError(f"Invoice with cart id '{filters["shopping_cart_id"]}' not found")

    if "status" in filters:
      if validate_column_and_query_value(conn, invoices_table, "status", filters["status"]):
        stmt = stmt.where(invoices_table.c.status == filters["status"])
      else:
        raise InvoiceNotFoundError(f"Invoices with status '{filters["status"]}' not found")

    results = conn.execute(stmt)

    invoices = [dict(row._mapping) for row in results]

    if not invoices:
      raise InvoiceNotFoundError("No matching invoices found.")

    return invoices


  @with_connection
  def check_invoices(self, conn, user_id : int) -> Optional[int]:
    if not validate_column_and_query_value(conn, invoices_table, "user_id", user_id):
      raise InvoiceNotFoundError(f"Invoice not found")

    stmt = select(invoices_table).where(invoices_table.c.user_id == user_id)
    result = conn.execute(stmt)
    invoices = [dict(row._mapping) for row in result]

    return invoices