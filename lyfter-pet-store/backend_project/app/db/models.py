from app.db.database import engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Numeric, DateTime, ForeignKey, Enum, func, Boolean, text, Computed, CheckConstraint

metadata_obj = MetaData(schema="pets_eccomerce")

user_table = Table(
  "users",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("name", String(50), nullable=False),
  Column("last_name", String(50), nullable=False),
  Column("email", String(50), nullable=False, unique=True),
  Column("password", String(250), nullable=False),
  Column("phone_number", String(25), nullable=False, unique=True),
  Column("is_admin", Boolean, nullable=False, server_default=text('false')),
  Column("created_at", DateTime, server_default=func.now())
)

products_table = Table(
  "products",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("name", String(255), nullable=False, unique=True),
  Column("price", Numeric(10, 2), nullable=False),
  Column("sku", String(8), nullable=False, unique=True),
  CheckConstraint("char_length(sku) = 8", name="sku_8_characters"),
  Column("category_id", ForeignKey("product_categories.id"), nullable=False),
  Column("stock", Integer, nullable=False, default=0),
  Column("entry_date", DateTime, server_default=func.now())
)

product_categories_table = Table(
  "product_categories",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("name", String(50), nullable=False, unique=True)
)

cart_table = Table(
  "carts",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("user_id", ForeignKey("users.id"), nullable=False),
  Column("status", Enum("active", "closed", "abandoned", "expired", name="status_enum"), nullable=False, default="active"),
  Column("created_at", DateTime, server_default=func.now()),
  Column("expires_at", DateTime, Computed("created_at + interval '1 hour'", persisted=True)),
)

cart_products_table = Table(
  "cart_products",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("cart_id", ForeignKey("carts.id"), nullable=False),
  Column("product_id", ForeignKey("products.id"), nullable=False),
  Column("quantity", Integer, nullable=False),
  Column("price", Numeric(10, 2), nullable=False),
)

shipping_address_table = Table(
  "shipping_address",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("street", String(255), nullable=False, unique=True),
  Column("city", String(100), nullable=False),
  Column("province", String(50), nullable=False),
  Column("zip_code", String(50), nullable=False),
  Column("country", String(50), nullable=False),
  Column("created_at", DateTime, server_default=func.now())
)

invoices_table = Table(
  "invoices",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("invoice_number", String(10), nullable=False, unique=True),
  CheckConstraint("char_length(invoice_number) = 10", name="invoice_number_10_characters"),
  Column("user_id", ForeignKey("users.id"), nullable=False),
  Column("cart_id", ForeignKey("carts.id"), nullable=False),
  Column("payment_method_id", ForeignKey("payment_method.id"), nullable=False),
  Column("total", Numeric(10, 2), nullable=False),
  Column("status", Enum("paid", "pending", "canceled", name="invoice_status_enum"), nullable=False),
  Column("shipping_address_id", ForeignKey("shipping_address.id"), nullable=False),
  Column("created_at", DateTime, server_default=func.now())
)

payment_method_table = Table(
  "payment_method",
  metadata_obj,
  Column("id", Integer, primary_key=True),
  Column("payment_method", Enum("sinpe", "card", "cash", name="payment_method_enum"), nullable=False)
)

if __name__ == "__main__":
  metadata_obj.create_all(engine)