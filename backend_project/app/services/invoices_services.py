from sqlalchemy import select
from db.models import invoices_table
from exceptions.exceptions import NotFoundError

class InvoicesServices:
  def __init__(self, invoices_validator, invoices_repository):
    self.invoices_validator = invoices_validator
    self.invoices_repository = invoices_repository


  def list_invoices(self, params : dict) -> list[dict]:
    filters  = self.invoices_validator.validate_filters(params)

    stmt = (select(
      invoices_table.c.id,
      invoices_table.c.invoice_number,
      invoices_table.c.user_id,
      invoices_table.c.cart_id,
      invoices_table.c.payment_method_id,
      invoices_table.c.total,
      invoices_table.c.status,
      invoices_table.c.shipping_address_id
    ))

    if "id" in filters:
      stmt = stmt.where(invoices_table.c.id == filters["id"])

    if "user_id" in filters:
      stmt = stmt.where(invoices_table.c.user_id == filters["user_id"])

    if "cart_id" in filters:
      stmt = stmt.where(invoices_table.c.cart_id == filters["cart_id"])

    if "payment_method_id" in filters:
      stmt = stmt.where(invoices_table.c.payment_method_id == filters["payment_method_id"])

    if "total" in filters:
      stmt = stmt.where(invoices_table.c.total == filters["total"])

    if "status" in filters:
      stmt = stmt.where(invoices_table.c.status == filters["status"])

    if "shipping_address_id" in filters:
      stmt = stmt.where(invoices_table.c.shipping_address_id == filters["shipping_address_id"])

    result = self.invoices_repository.get_invoices(stmt)
  
    invoices = [dict(row._mapping) for row in result]

    if not invoices:
      raise NotFoundError("No matching invoices found.")

    return invoices


  def get_user_invoices(self, user_id: int):

    invoices = self.invoices_repository.get_user_invoices(user_id)

    if not invoices:
      raise NotFoundError(f"Invoices for {user_id} not found.")

    return invoices