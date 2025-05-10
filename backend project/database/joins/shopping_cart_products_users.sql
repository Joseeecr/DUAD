SET search_path TO pets_eccomerce;

SELECT 
  shopping_cart_products.id AS shopping_cart_products_id,
  shopping_cart_products.amount AS amount_of_products,
  shopping_cart_products.shopping_cart_id,
  products.name AS product_name,
  users.name AS user_name,
  users.user_email,
  users.id as user_id
FROM shopping_cart_products
INNER JOIN products ON shopping_cart_products.product_id = products.id
INNER JOIN shopping_cart ON shopping_cart_products.shopping_cart_id = shopping_cart.id 
INNER JOIN users on shopping_cart.user_id = users.id;