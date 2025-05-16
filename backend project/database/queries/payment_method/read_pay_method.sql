-- get all data
SELECT id, payment_method
FROM pets_eccomerce.payment_method
ORDER BY id ASC;

-- get specific payment_method by payment_method name
SELECT id, payment_method
FROM pets_eccomerce.payment_method WHERE payment_method = :payment_method;

-- get payment by id
SELECT id, payment_method
FROM pets_eccomerce.payment_method WHERE id = :id;

-- get id based on payment_method's name
SELECT id
FROM pets_eccomerce.payment_method WHERE payment_method = :payment_method;