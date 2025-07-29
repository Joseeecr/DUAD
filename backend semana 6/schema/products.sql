SET search_path TO transactions_practice;

CREATE TABLE IF NOT EXISTS products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(250) NOT NULL UNIQUE,
	sku char(8) NOT NULL UNIQUE,
	stock smallint NOT NULL
);