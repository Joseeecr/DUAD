-- get all invoices without filters
SELECT id, invoice_number, payment_method_id, created_date, user_id, total_price, shopping_cart_id, shipping_address_id
FROM pets_eccomerce.invoices 
ORDER BY id ASC;

-- get invoices based on invoice_number. Replace :invoice_number with invoice_number
SELECT id, invoice_number, payment_method_id, created_date, user_id, total_price, shopping_cart_id, shipping_address_id
FROM pets_eccomerce.invoices  WHERE invoice_number = :invoice_number;

-- get invoice info based on user_id. Replace :user_id with user's id
SELECT id, invoice_number, created_date
FROM pets_eccomerce.invoices  WHERE user_id = :user_id;

-- Get invoices based on a specific created date. Replace :created_date with a valid date
SELECT id, invoice_number, payment_method_id, created_date, user_id, total_price, shopping_cart_id, shipping_address_id
FROM pets_eccomerce.invoices  WHERE created_date = :created_date
ORDER BY id ASC;

-- Get invoices created in a range of dates
SELECT id, invoice_number, payment_method_id, created_date, user_id, total_price, shopping_cart_id, shipping_address_id
FROM pets_eccomerce.invoices  WHERE created_date BETWEEN :created_date AND :created_date
ORDER BY created_date ASC;