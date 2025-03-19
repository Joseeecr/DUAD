ALTER TABLE invoices
    ADD COLUMN buyer_phone_number BIGINT NOT NULL DEFAULT 0;

ALTER TABLE invoices
    ADD COLUMN employee_code CHAR(5) NOT NULL DEFAULT 'hello';

-- UPDATE invoices SET
--     buyer_phone_number = 70324433,
--     employee_code = '#1'
-- WHERE id == 1;

-- UPDATE invoices SET
--     buyer_phone_number = 80093322,
--     employee_code = '#3'
-- WHERE id == 2;

-- ALTER TABLE invoices
--     Rename COLUMN total_prize to total_price;
-- DROP TABLE products_carts;
-- UPDATE invoices SET
-- purchase_date ='2025-02-01'
-- WHERE id = 1;

-- Update  invoices SET
-- purchase_date ='2025-02-01'
-- WHERE id = 2;
-- DELETE FROM products_carts;
-- Update  invoices SET
-- total_price = 48000
-- WHERE id = 2;

SELECT *
    FROM products;

SELECT *
    FROM products
    WHERE price > 50000;

SELECT *
    FROM products_carts
    WHERE product_id = 2;

SELECT *
    FROM products_carts
    WHERE product_id = 3;

SELECT product_id, SUM(total_products)
    FROM products_invoices
    GROUP BY product_id;

SELECT *
    FROM invoices
    WHERE user_email = 'armando@yahoo.com';


SELECT *
    FROM invoices
    ORDER by total_price DESC;

SELECT *
    FROM invoices
    WHERE invoice_number = 'F-2025-1';


