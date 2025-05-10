SET search_path TO pets_eccomerce;

SELECT 
  products.id AS product_id, 
  products.name AS product_name, 
  categories.category
FROM products
INNER JOIN categories on products.category_id = categories.id
ORDER BY products.id ASC;