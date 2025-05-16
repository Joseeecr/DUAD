-- get all data
SELECT id, category
FROM pets_eccomerce.categories
ORDER BY id ASC;

-- get specific category by category name
SELECT category
FROM pets_eccomerce.categories WHERE category = :category;

-- get specific category by id
SELECT category
FROM pets_eccomerce.categories WHERE id = :id;

-- get id based on category's name
SELECT id
FROM pets_eccomerce.categories WHERE category = :category;