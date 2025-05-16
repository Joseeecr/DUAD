CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	user_email varchar(50) NOT NULL UNIQUE,
	password VARCHAR(30) NOT NULL,	
	phone_number bigint UNIQUE NOT NULL,
  role_id INT REFERENCES roles(id) NOT NULL,
	created_date DATE DEFAULT CURRENT_DATE
)