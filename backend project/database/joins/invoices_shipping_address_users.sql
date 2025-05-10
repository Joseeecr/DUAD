--get the information about pay method, users, invoices and shipping address

SET search_path TO pets_eccomerce;

SELECT 
  invoices.id AS invoice_id,
  users.id AS user_id,
  invoices.invoice_number,
  invoices.created_date,
  payment_method.payment_method,
  users.name AS user_name,
  users.last_name,
  users.user_email,
  shipping_address.id AS shipping_address_id,
  shipping_address.street,
  shipping_address.city,
  shipping_address.province,
  shipping_address.country
FROM invoices
INNER JOIN payment_method on invoices.payment_method_id = payment_method.id
INNER JOIN users on invoices.user_id = users.id
INNER JOIN shipping_address ON invoices.shipping_address_id = shipping_address.id;