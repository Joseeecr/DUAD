--get all registers
SELECT id, amount, product_id, shopping_cart_id
FROM pets_eccomerce.shopping_cart_products
ORDER BY id ASC;

--get the information based on the id
SELECT id, amount, product_id, shopping_cart_id
FROM pets_eccomerce.shopping_cart_products WHERE id = :id;