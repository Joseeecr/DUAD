SET search_path TO transactions_practice;

CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	phone_number BIGINT NOT NULL UNIQUE
);