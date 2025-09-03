from sqlalchemy import insert, select, delete, update, Select
from sqlalchemy.engine import CursorResult, Row
from app.db.models import cart_table, products_table, cart_products_table, payment_method_table, shipping_address_table
from app.repos.utils import with_connection
from typing import Optional

class CartsRepository:
  def __init__(self, engine):
    self.engine = engine

  @with_connection
  def get_carts(self, conn, stmt : Select) -> CursorResult:
    return conn.execute(stmt)


  def get_cart_by_id(self, session, table, id : int) -> Optional[Row]:
    stmt = select(table).where(table.c.id == id)
    result = session.execute(stmt).first()

    if result:
      return dict(result._mapping)
    return None


  def get_cart_id_by_user(self, session, user_id : int) -> Optional[int]:
    cart = session.execute(select(cart_table).where(
        (cart_table.c.user_id == user_id) &
        (cart_table.c.status == "active")
    )).fetchone()

    if not cart:
      return None

    return cart.id


  def insert_cart_if_needed(self, session, user_id : int) -> Optional[int]:
    stmt = insert(cart_table).returning(cart_table.c.id).values(user_id=user_id)
    result = session.execute(stmt)
    return result.scalar_one()


  def get_product_by_id(self, session, product_id : int) -> Optional[int]:
    product = session.execute(select(products_table).where(
        (products_table.c.id == product_id)
    )).fetchone()

    if not product:
      return None

    return product


  def get_cart_product_entry(self, session, cart_id : int, product_id : int) -> Optional[int]:
    existing = session.execute(select(cart_products_table).where(
        (cart_products_table.c.cart_id == cart_id) &
        (cart_products_table.c.product_id == product_id)
    )).fetchone()

    return existing


  def update_quantity_if_cart_product_already_exists(self, session, existing_cart, quantity, cart_id, product_id) -> Optional[int]:
    new_quantity = existing_cart.quantity + quantity

    result = session.execute(update(cart_products_table)
                  .where(
                    (cart_products_table.c.cart_id == cart_id) &
                    (cart_products_table.c.product_id == product_id)
                  )
                  .values(quantity=new_quantity))

    return result


  def add_data_to_cart_if_cart_product_doesnt_exist(self, session, cart_id : int, product_id : int, quantity : int, price: int) -> Optional[int]:
    result = session.execute(insert(cart_products_table).values(
        cart_id=cart_id,
        product_id=product_id,
        quantity=quantity,
        price=price
      ))

    return result


  def get_payment_method(self, session, payment_method):
    payment_method = session.execute(select(payment_method_table).where(
        (payment_method_table.c.payment_method == payment_method)
    )).fetchone()

    if not payment_method:
      return None

    return payment_method.id


  def get_shipping_address(self, session, shipping_address_id):
    address = session.execute(select(shipping_address_table).where(
        (shipping_address_table.c.id == shipping_address_id)
    )).fetchone()

    if not address:
      return None

    return address.id


  def update_cart(self, session, id : int, data : dict) -> int:

    stmt = (
      update(cart_table).returning(cart_table.c.id)
      .where(cart_table.c.id == id)
      .values(**data)
    )

    result = session.execute(stmt)
    return result.scalar_one()


  def update_cart_items(self, session, cart_id : int,  product_id : int, data : dict) -> int:

    stmt = (
      update(cart_products_table).returning(cart_products_table.c.id)
      .where(
        (cart_products_table.c.cart_id == cart_id) &
        (cart_products_table.c.product_id == product_id)
    )
      .values(**data)
    )

    result = session.execute(stmt)
    return result.scalar_one()


  def get_existing_address(self, session, address_data : dict) -> Optional[int]:

    existing = session.execute(select(shipping_address_table).where(
        (shipping_address_table.c.street == address_data.get("street")) &
        (shipping_address_table.c.city == address_data.get("city")) &
        (shipping_address_table.c.province == address_data.get("province")) &
        (shipping_address_table.c.zip_code == address_data.get("zip_code")) &
        (shipping_address_table.c.country == address_data.get("country"))
    )).fetchone()

    if existing is None:
        return None

    return existing.id


  def insert_address_if_needed(self, session, address_data : dict) -> Optional[int]:

    stmt = insert(shipping_address_table).values(
        street=address_data.get("street"),
        city=address_data.get("city"),
        province=address_data.get("province"),
        zip_code=address_data.get("zip_code"),
        country=address_data.get("country"),
    ).returning(shipping_address_table.c.id)

    result = session.execute(stmt)
    return result.scalar_one()
