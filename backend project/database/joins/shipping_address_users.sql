SET search_path TO pets_eccomerce;

SELECT 
  shipping_address.id AS shipping_address_id,
  shipping_address.street,
  shipping_address.city,
  shipping_address.province,
  shipping_address.country,
  users.name AS user_name,
  users.last_name AS user_last_name,
  users.user_email,
  users.id as user_id
FROM shipping_address
INNER JOIN users ON shipping_address.user_id = users.id;