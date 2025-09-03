from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Numeric, DateTime, ForeignKey, Enum, func
from db.db_manager import DbConnection

conn = DbConnection()
engine = conn.engine
metadata_obj = MetaData(schema="jwt_practice")

user_table = Table(
  "users",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("username", String(30), nullable=False),
  Column("password", String, nullable=False),
  Column("role_id", ForeignKey("roles.id"), nullable=False)
)

roles_table = Table(
  "roles",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("role", Enum("admin", "user", name="role_enum"), nullable=False),
)

products_table = Table(
  "products",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("name", String(30), nullable=False),
  Column("price", Numeric(10, 2), nullable=False),
  Column("entry_date", DateTime, server_default=func.now()),
  Column("quantity", Integer),
)

shopping_cart_table = Table(
  "shopping_carts",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("user_id", ForeignKey("users.id"), nullable=False),
  Column("status", Enum("active", "closed", "canceled", name="status_enum"), nullable=False),
  Column("created_at", DateTime, server_default=func.now()),
)

cart_items_table = Table(
  "cart_items",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("shopping_cart_id", ForeignKey("shopping_carts.id"), nullable=False),
  Column("product_id", ForeignKey("products.id"), nullable=False),
  Column("quantity", Integer, nullable=False),
  Column("price", Numeric(10, 2), nullable=False),
)

invoices_table = Table(
  "invoices",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("user_id", ForeignKey("users.id"), nullable=False),
  Column("shopping_cart_id", ForeignKey("shopping_carts.id"), nullable=False),
  Column("created_at", DateTime, server_default=func.now()),
  Column("total", Numeric(10, 2), nullable=False),
  Column("status", Enum("paid", "pending", "canceled", name="invoice_status_enum"), nullable=False),
)

if __name__ == "__main__":
  metadata_obj.create_all(engine)