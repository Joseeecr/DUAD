SET search_path TO transactions_practice;

CREATE TABLE IF NOT EXISTS invoices (
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id) NOT NULL,
	product_id INT REFERENCES products(id) NOT NULL,
	total NUMERIC(12,2) NOT NULL,
	status VARCHAR(20) NOT NULL,
  date TIMESTAMP DEFAULT now()
  );