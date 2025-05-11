SET search_path TO pets_eccomerce;

--get products and their categories
SELECT 
  products.id AS product_id, 
  products.name AS product_name, 
  categories.category
FROM products
INNER JOIN categories on products.category_id = categories.id
ORDER BY products.id ASC;

SELECT 
  categories.category AS category_name, 
  COUNT(products.category_id) as total
FROM categories
INNER JOIN products on categories.id = products.category_id
GROUP BY (categories.category)
ORDER BY total DESC;