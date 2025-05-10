--Get info of cart based on user_id. Replace :user_id with the user_id
SELECT id, status, created_date, expires_at, user_id
FROM pets_eccomerce.shopping_cart WHERE user_id = :user_id;

--Get cart based on cart id. Replace :id with the cart id
SELECT id, status, created_date, expires_at, user_id
FROM pets_eccomerce.shopping_cart WHERE id = :id;

--Get carts based on status. Replace :status with a valid status
SELECT id, status, created_date, expires_at, user_id
FROM pets_eccomerce.shopping_cart WHERE status = :status
ORDER BY id ASC;

--Replace :created_date with the date
SELECT id, status, created_date, expires_at, user_id
FROM pets_eccomerce.shopping_cart WHERE DATE(created_date) = :created_date
ORDER BY id ASC;