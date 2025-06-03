SET search_path TO orms_practice;

CREATE TABLE cars (
	id SERIAL PRIMARY KEY,
	Make VARCHAR(25) NOT NULL,
	Model VARCHAR(30) NOT NULL,
	year_of_manufacture SMALLINT NOT NULL,
	user_id INT REFERENCES users(id),
  created_date TIMESTAMP DEFAULT now()
);