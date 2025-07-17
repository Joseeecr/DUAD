CREATE TABLE IF NOT EXISTS roles (
	id SERIAL PRIMARY KEY,
	role varchar(20),
	CHECK (LOWER(rol) IN ('cliente', 'admin'))
);