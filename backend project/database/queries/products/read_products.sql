--get all products
SELECT id, name, price, category_id, sku, stock, created_date
FROM pets_eccomerce.products ORDER BY id ASC;

-- get products based on SKU. Replace :SKU with SKU
SELECT id, name, price, category_id, sku, stock, created_date
FROM pets_eccomerce.products  WHERE sku = :sku;

-- get products based on name. Replace :name with name
SELECT id, name, price, category_id, sku, stock, created_date
FROM pets_eccomerce.products  WHERE name = :name;

-- get products based on a range of dates. Replace :created_date with created_date
SELECT id, name, price, category_id, sku, stock, created_date
FROM pets_eccomerce.products  WHERE created_date BETWEEN :created_date AND :created_date
ORDER BY created_date ASC;