--get all shipping_addresses without filters
SELECT id, street, city, province, zip_code, country, created_date, user_id
FROM pets_eccomerce.shipping_address 
ORDER BY id ASC;

--get shipping address based on id
SELECT id, street, city, province, zip_code, country, created_date, user_id
FROM pets_eccomerce.shipping_address WHERE id = :id

--get shipping addressess based on user_id
SELECT id, street, city, province, zip_code, country, created_date, user_id
FROM pets_eccomerce.shipping_address WHERE user_id = :user_id
ORDER BY id ASC;

--get shipping_address based on street. Replace :street with street
  SELECT id, street, city, province, zip_code, country, user_id
  FROM pets_eccomerce.shipping_address WHERE street = :street;

--get shipping_address info based on zip_code. Replace :zip_code with a zip_code enclosed
--in a pair of single or double quotes
SELECT id, street, city, zip_code, province, country, user_id
FROM pets_eccomerce.shipping_address WHERE zip_code = :zip_code;

--get shipping_address based on a specific created_date. Replace :created_date with a valid date
SELECT id, street, city, province, zip_code, country, created_date, user_id
FROM pets_eccomerce.shipping_address WHERE DATE(created_date) = :created_date
ORDER BY id ASC;

--get shipping_address based on a province
SELECT id, street, city, zip_code, province, country, user_id
FROM pets_eccomerce.shipping_address WHERE province = :province;

--get shipping_address created in a range of dates
SELECT id, street, city, province, zip_code, country, created_date, user_id
FROM pets_eccomerce.shipping_address WHERE DATE(created_date) BETWEEN :created_date AND :created_date
ORDER BY created_date ASC;

--group the amount of users by countries 
SELECT
	country, 
	COUNT(DISTINCT user_id) AS total_users
FROM pets_eccomerce.shipping_address
GROUP BY country;

--group the amount of users by provinces 
SELECT
	province, 
	COUNT(DISTINCT user_id) AS total_users
FROM pets_eccomerce.shipping_address
GROUP BY province

