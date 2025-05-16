CREATE TABLE IF NOT EXISTS shopping_cart_products (
  id SERIAL PRIMARY KEY,
  amount INT NOT NULL,
  product_id INT REFERENCES products(id),
  shopping_cart_id INT REFERENCES shopping_cart(id)
);