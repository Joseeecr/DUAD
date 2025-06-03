SET search_path TO orms_practice;

CREATE TABLE IF NOT EXISTS addresses (
  id SERIAL PRIMARY KEY,
  street VARCHAR(250) UNIQUE NOT NULL,
  city VARCHAR(50) NOT NULL,
  province VARCHAR(50) NOT NULL,
  zip_code VARCHAR(50) NOT NULL,
  country VARCHAR(50) NOT NULL,
  user_id INT REFERENCES users(id),
  created_date TIMESTAMP DEFAULT now()
);