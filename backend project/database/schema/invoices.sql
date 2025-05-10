CREATE TABLE IF NOT EXISTS invoices (
  id SERIAL PRIMARY KEY,
  invoice_number CHAR(8) UNIQUE NOT NULL,
  payment_method_id INT REFERENCES payment_method(id) NOT NULL,
  user_id INT REFERENCES users(id) NOT NULL,
  total_price NUMERIC(12,2) NOT NULL,
  shopping_cart_id INT REFERENCES shopping_cart(id) UNIQUE NOT NULL,
  shipping_address_id INT REFERENCES shipping_address(id) NOT NULL,
  created_date TIMESTAMP DEFAULT now()
);