# SET search_path TO orms_practice;

# CREATE TABLE IF NOT EXISTS addresses (
#   id SERIAL PRIMARY KEY,
#   street VARCHAR(250) UNIQUE NOT NULL,
#   city VARCHAR(50) NOT NULL,
#   province VARCHAR(50) NOT NULL,
#   zip_code VARCHAR(50) NOT NULL,
#   country VARCHAR(50) NOT NULL,
#   user_id INT REFERENCES users(id),
#   created_date TIMESTAMP DEFAULT now()
# );

# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 0, Avenida Central', 'San José', 'San José', '10101', 'Costa Rica', 5);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle La Cruz', 'Liberia', 'Guanacaste', '50101', 'Costa Rica', 2);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 1, Barrio Los Ángeles', 'Cartago', 'Cartago', '30101', 'Costa Rica', 3);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle 5, Urbanización La Trinidad', 'Heredia', 'Heredia', '40101', 'Costa Rica', 1);
# insert into addresses (street, city, province, zip_code, country, user_id) values ('Calle Central, Barrio Los Ángeles', 'Alajuela', 'Alajuela', '20101', 'Costa Rica', 4);