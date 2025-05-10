-- get all data
SELECT id, role
FROM pets_eccomerce.roles
ORDER BY id ASC;

-- get specific role by role name
SELECT id, role
FROM pets_eccomerce.roles WHERE role = :role;

-- get role by id
SELECT id, role
FROM pets_eccomerce.roles WHERE id = :id;

-- get id based on role's name
SELECT id
FROM pets_eccomerce.roles WHERE role = :role;