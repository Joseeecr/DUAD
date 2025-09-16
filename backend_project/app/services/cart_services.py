from sqlalchemy import select, update, insert
from app.db.models import cart_table, cart_products_table, products_table, invoices_table
from app.db.session import SessionLocal
from app.exceptions.exceptions import NotFoundError
import random
import string

class CartServices:
  def __init__(self, carts_validator, carts_repository):
    self.carts_validator = carts_validator
    self.carts_repository = carts_repository


  def list_carts(self, params : dict) -> list[dict]:
    filters  = self.carts_validator.validate_filters(params)

    stmt = (select(
      cart_table.c.id,
      cart_table.c.user_id,
      cart_table.c.status,
      cart_table.c.created_at,
      cart_table.c.expires_at
    ))

    if "id" in filters:
      stmt = stmt.where(cart_table.c.id == filters["id"])

    if "user_id" in filters:
      stmt = stmt.where(cart_table.c.user_id == filters["user_id"])

    if "status" in filters:
      stmt = stmt.where(cart_table.c.status == filters["status"])

    result = self.carts_repository.get_carts(stmt)
  
    carts = [dict(row._mapping) for row in result]

    if not carts:
      raise NotFoundError("No matching carts found.")

    return carts


  def add_product_to_cart(self, user_id: int, data : dict):

    with SessionLocal() as session:
      with session.begin():
        cart_id = self.carts_repository.get_cart_id_by_user(session, user_id)
        validate_payload = self.carts_validator.validate_insert_products_to_cart(data)

        product = self.carts_repository.get_product_by_id(session, validate_payload.get("product_id"))
        
        if not product:
          raise NotFoundError(f"Product not found.")

        if cart_id is None:
          cart_id = self.carts_repository.insert_cart_if_needed(session, user_id)

        #*check if cart already exists in cart_products table
        existing = self.carts_repository.get_cart_product_entry(session, cart_id, validate_payload.get("product_id"))

        if existing:
          return self.carts_repository.update_quantity_if_cart_product_already_exists(session, existing, validate_payload.get("quantity"), cart_id, validate_payload.get("product_id"))
        else:
          return self.carts_repository.add_data_to_cart_if_cart_product_doesnt_exist(session, cart_id, validate_payload.get("product_id"), validate_payload.get("quantity"), product.price)


  def generate_invoice_number(self):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=10))


  def get_or_create_address(self, session, address_data: dict) -> int:
    existing_id = self.carts_repository.get_existing_address(session, address_data)
    if existing_id is not None:
      return existing_id
    return self.carts_repository.insert_address_if_needed(session, address_data)


  def checkout_cart(self, user_id: int, data : dict):
    with SessionLocal() as session:
      with session.begin():

        validate_payload = self.carts_validator.validate_create_invoice(data)
        shipping_address_data = validate_payload.get("shipping_address")
        shipping_address_id = self.get_or_create_address(session, shipping_address_data)

        #*Check the cart exists and is active
        shopping_cart_id = self.carts_repository.get_cart_id_by_user(session, user_id)

        if shopping_cart_id is None:
          raise NotFoundError(f"Not found.")

        items = self.carts_repository.get_cart_products(session, shopping_cart_id)
        
        for item in items:
          product = self.carts_repository.get_product_by_id(session, item.product_id)

          if not product:
            raise NotFoundError("Product not found")

          if product.stock < item.quantity:
            raise Exception(f"Not enough stock for product '{product.name}'")

          new_stock = product.stock - item.quantity

          self.carts_repository.update_product_stock(session, item.product_id, new_stock)

        self.carts_repository.close_cart(session, shopping_cart_id)

        total = sum(item.quantity * item.price for item in items)

        invoice_number = self.generate_invoice_number()
        payment_method_id = self.carts_repository.get_payment_method(session, validate_payload.get("payment_method"))

        invoice_id = self.carts_repository.create_invoice(
          session,
          user_id,
          shopping_cart_id,
          payment_method_id,
          total,
          shipping_address_id,
          invoice_number
        )

        return invoice_id


  def update_cart_by_admin(self, carts_id : int, data : dict):
    with SessionLocal() as session:
      with session.begin():
        cart = self.carts_repository.get_cart_by_id(session, cart_table, carts_id)

        if not cart:
          raise ValueError("cart not found")
        
        validate_data = self.carts_validator.validate_update_cart_admin(data)

        return self.carts_repository.update_cart(session, carts_id, validate_data)


  def update_cart_products(self, user_id : int, data : dict):
    with SessionLocal() as session:
      with session.begin():
        cart_id = self.carts_repository.get_cart_id_by_user(session, user_id)

        if not cart_id:
          raise ValueError("cart not found")
        
        validate_data = self.carts_validator.validate_insert_products_to_cart(data)
        
        return self.carts_repository.update_cart_items(session, cart_id, validate_data.get("product_id"), validate_data)