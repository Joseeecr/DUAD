CREATE TABLE lyfter_car_rental.users_cars(
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES lyfter_car_rental.users(id),
	car_id INT REFERENCES lyfter_car_rental.cars(id),
	rental_date DATE NOT NULL,
	rental_status VARCHAR(30) NOT NULL
);

insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (1, 1, '16/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (2, 2, '27/01/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (3, 3, '18/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (4, 4, '14/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (5, 5, '02/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (6, 6, '24/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (7, 7, '14/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (8, 8, '23/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (9, 9, '02/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (10, 10, '09/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (11, 11, '24/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (12, 12, '07/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (13, 13, '20/02/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (14, 14, '30/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (15, 15, '11/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (16, 16, '17/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (17, 17, '24/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (18, 18, '01/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (19, 19, '06/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (20, 20, '01/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (21, 21, '24/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (22, 22, '12/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (23, 23, '02/01/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (24, 24, '22/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (25, 25, '07/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (26, 26, '08/02/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (27, 27, '07/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (28, 28, '25/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (29, 29, '04/02/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (30, 30, '01/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (31, 31, '17/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (32, 32, '08/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (33, 33, '21/02/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (34, 34, '10/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (35, 35, '17/01/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (36, 36, '26/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (37, 37, '14/02/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (38, 38, '19/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (39, 39, '11/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (40, 40, '07/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (41, 41, '10/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (42, 42, '01/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (43, 43, '04/01/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (44, 44, '28/03/2025', 'Active');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (45, 45, '21/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (46, 46, '11/01/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (47, 47, '09/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (48, 48, '24/03/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (49, 49, '01/02/2025', 'Completed');
insert into lyfter_car_rental.users_cars (user_id, car_id, rental_date, rental_status) values (50, 50, '02/03/2025', 'Completed');