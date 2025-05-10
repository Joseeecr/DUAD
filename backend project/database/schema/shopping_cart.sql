CREATE TABLE IF NOT EXISTS shopping_cart (
  id SERIAL PRIMARY KEY,
  status varchar(20),
  CHECK (LOWER(status) IN ('Active', 'Closed', 'Expired', 'Discarded')),
  created_date TIMESTAMP DEFAULT now(),
  expires_at TIMESTAMP GENERATED ALWAYS AS (created_at + interval '1 hour') STORED
  user_id INT REFERENCES users(id)
);