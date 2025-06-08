# SET search_path TO orms_practice;

# CREATE TABLE cars (
# 	id SERIAL PRIMARY KEY,
# 	Make VARCHAR(25) NOT NULL,
# 	Model VARCHAR(30) NOT NULL,
# 	year_of_manufacture SMALLINT NOT NULL,
# 	user_id INT REFERENCES users(id),
#   created_date TIMESTAMP DEFAULT now()
# );

# insert into cars (Make, Model, year_of_manufacture, user_id) values ('Cadillac', 'STS', 2007, 3);
# insert into cars (Make, Model, year_of_manufacture, user_id) values ('Maserati', 'Spyder', 1991, 4);
# insert into cars (Make, Model, year_of_manufacture, user_id) values ('GMC', 'Savana 2500', 2008, 5);
# insert into cars (Make, Model, year_of_manufacture, user_id) values ('Chevrolet', 'Astro', 1994, 1);
# insert into cars (Make, Model, year_of_manufacture, user_id) values ('Infiniti', 'QX', 2007, 2);