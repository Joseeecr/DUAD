SET search_path TO pets_eccomerce;
SELECT
  users.id AS user_id,
  users.name AS user_name, 
  users.last_name, 
  users.user_email, 
  roles.role AS user_role
FROM users 
INNER JOIN roles ON users.role_id = roles.id
ORder BY roles.role ASC;