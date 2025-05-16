SET search_path TO pets_eccomerce;
SELECT 
  users.id AS user_id, 
  users.name, 
  users.last_name, 
  users.user_email, 
  shopping_cart.id AS shopping_cart_id, 
  shopping_cart.status
From users
INNER JOIN shopping_cart ON users.id = shopping_cart.user_id
ORDER BY user_id ASC;