from sqlalchemy import insert, select, delete, update
from db.tables import shopping_cart_table, user_table, products_table, cart_items_table, invoices_table
from repos.repos_utils import with_connection, validate_column_and_query_value
from exceptions.generated_exceptions import CartNotFoundError, UserNotFoundError, ProductNotFoundError

class ShoppingCartRepository:
  def __init__(self, engine, shopping_cart_validator):
    self.engine = engine
    self.shopping_cart_validator = shopping_cart_validator

  @with_connection
  def get_carts(self, conn, filters : dict) -> dict:
    stmt = select(shopping_cart_table)

    if "id" in filters:
      if validate_column_and_query_value(conn, shopping_cart_table,"id", filters["id"]):
        stmt = stmt.where(shopping_cart_table.c.id == filters["id"])
      else:
        raise CartNotFoundError(f"Cart with id {filters["id"]} not found")

    if "user_id" in filters:
      if validate_column_and_query_value(conn, shopping_cart_table, "user_id", filters["user_id"]):
        stmt = stmt.where(shopping_cart_table.c.user_id == filters["user_id"])
      else:
        raise CartNotFoundError(f"Cart with user id '{filters["user_id"]}' not found")
  
    if "status" in filters:
      if validate_column_and_query_value(conn, shopping_cart_table, "status", filters["status"]):
        stmt = stmt.where(shopping_cart_table.c.status == filters["status"])
      else:
        raise CartNotFoundError(f"Cart with status '{filters["status"]}' not found")

    if "created_from" in filters:
      if validate_column_and_query_value(conn, shopping_cart_table, "created_at", filters["created_from"]):
        stmt = stmt.where(shopping_cart_table.c.created_at >= filters["created_from"])
      else:
        raise CartNotFoundError(f"Cart with date '{filters["created_from"]}' not found")

    if "created_to" in filters:
      if validate_column_and_query_value(conn, shopping_cart_table, "created_at", filters["created_to"]):
        stmt = stmt.where(shopping_cart_table.c.created_at >= filters["created_to"])
      else:
        raise CartNotFoundError(f"Cart with date '{filters["created_to"]}' not found")

    results = conn.execute(stmt)
    shopping_carts = [dict(row._mapping) for row in results]

    if not shopping_carts:
      raise CartNotFoundError("No matching carts found.")

    return shopping_carts


  @with_connection
  def insert_cart(self, conn, user_id : int) -> int:

    if validate_column_and_query_value(conn, user_table, "id", user_id):
      stmt = insert(shopping_cart_table).returning(shopping_cart_table.c.id).values(user_id=user_id)
      result = conn.execute(stmt)
      conn.commit()
      return result.scalar_one()
    else:
      raise UserNotFoundError(f"User with id {user_id} not found")


  @with_connection
  def add_product_to_cart(self, conn, shopping_cart_id: int, product_id: int, quantity: int):

    cart = validate_column_and_query_value(conn, shopping_cart_table, "id", shopping_cart_id)
    if not cart:
      raise CartNotFoundError(f"Cart with id '{shopping_cart_id}' not found.")

    product = validate_column_and_query_value(conn, products_table, "id", product_id)
    if not product:
      raise ProductNotFoundError(f"Product with id '{product_id}' not found.")

    #*check if cart already exists
    existing = conn.execute(select(cart_items_table).where(
        (cart_items_table.c.shopping_cart_id == shopping_cart_id) &
        (cart_items_table.c.product_id == product_id)
    )).fetchone()

    if existing:
      new_quantity = existing.quantity + quantity
      conn.execute(update(cart_items_table)
                  .where(
                    (cart_items_table.c.shopping_cart_id == shopping_cart_id) &
                    (cart_items_table.c.product_id == product_id)
                  )
                  .values(quantity=new_quantity))
    else:
      conn.execute(insert(cart_items_table).values(
        shopping_cart_id=shopping_cart_id,
        product_id=product_id,
        quantity=quantity,
        price=product.price
      ))

    conn.commit()


  @with_connection
  def update_cart(self, conn, id : int, data : dict) -> int:
    if not validate_column_and_query_value(conn, shopping_cart_table, "id", id):
      return False

    stmt = (
      update(shopping_cart_table).returning(shopping_cart_table.c.id)
      .where(shopping_cart_table.c.id == id)
      .values(**data)
    )

    result = conn.execute(stmt)
    conn.commit()
    return result.scalar_one()


  @with_connection
  def delete_cart(self, conn, _id : int) -> bool:
    if not validate_column_and_query_value(conn, shopping_cart_table, "id", _id):
      return False

    stmt = delete(shopping_cart_table).where(shopping_cart_table.c.id == _id)
    conn.execute(stmt)
    conn.commit()
    return True


  @with_connection
  def close_cart(self, conn, shopping_cart_id: int):
    
    #*Check the cart exists and is in active
    cart = conn.execute(select(shopping_cart_table).where(shopping_cart_table.c.id == shopping_cart_id)).first()
    if not cart:
      raise CartNotFoundError(f"Cart with id '{shopping_cart_id}' not found.")

    if cart.status != "active":
      raise Exception("Cart is not in a closable state.")

    items = conn.execute(
        select(cart_items_table).where(cart_items_table.c.shopping_cart_id == shopping_cart_id)
    ).fetchall()
    
    for item in items:
      product = conn.execute(
        select(products_table).where(products_table.c.id == item.product_id)
      ).fetchone()

      if not product or product.quantity < item.quantity:
        raise Exception(f"Not enough stock for product {item.product_id}")

      conn.execute(update(products_table)
          .where(products_table.c.id == item.product_id)
          .values(quantity=products_table.c.quantity - item.quantity))

    conn.execute(update(shopping_cart_table)
        .where(shopping_cart_table.c.id == shopping_cart_id)
        .values(status="closed"))

    total = sum(item.quantity * item.price for item in items)

    invoice_stmt = insert(invoices_table).returning(invoices_table.c.id).values(
        user_id=cart.user_id,
        shopping_cart_id=shopping_cart_id,
        total=total,
        status="paid"
    )
    invoice_id = conn.execute(invoice_stmt).scalar_one()
    conn.commit()
    return invoice_id