# SET search_path TO orms_practice;

# CREATE TABLE IF NOT EXISTS users (
# 	id SERIAL PRIMARY KEY,
# 	name VARCHAR(20) NOT NULL,
# 	email VARCHAR(50) NOT NULL UNIQUE,
# 	phone_number BIGINT NOT NULL UNIQUE,
#   created_date TIMESTAMP DEFAULT now()
# );

# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 0, Avenida Central', 'San José', 'San José', '10101', 'Costa Rica', 5);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle La Cruz', 'Liberia', 'Guanacaste', '50101', 'Costa Rica', 2);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 1, Barrio Los Ángeles', 'Cartago', 'Cartago', '30101', 'Costa Rica', 3);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 5, Urbanización La Trinidad', 'Heredia', 'Heredia', '40101', 'Costa Rica', 1);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle Central, Barrio Los Ángeles', 'Alajuela', 'Alajuela', '20101', 'Costa Rica', 4);