CREATE TABLE IF NOT EXISTS products (
	id SERIAL primary key,
	name VARCHAR(50) NOT NULL,
	price numeric(12,2) NOT NULL,
	category_id REFERENCES categories(id),
	sku char(8) NOT NULL UNIQUE,
	stock smallint NOT NULL,
	created_date DATE DEFAULT current_date
);