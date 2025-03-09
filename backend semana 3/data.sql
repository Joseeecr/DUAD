-- products table
INSERT INTO products(code, product_name, prize, pub_date, brand)
    VALUES('434jknm3', 'Tennis', 70000, 2025-1-11, 'Nike');

INSERT INTO products(code, product_name, prize, pub_date, brand)
    VALUES('5er221mn', 'Tshirt', 20000, '2025-01-20', 'Umbro');

INSERT INTO products(code, product_name, prize, pub_date, brand)
    VALUES('jas3i44n', 'Socks', 8000, '2025-01-24', 'Nike');

INSERT INTO products(code, product_name, prize, pub_date, brand)
    VALUES('mm341ssa', 'Shorts', 12000, '2025-01-25', 'Adidas');


-- invoices table
INSERT INTO invoices(invoice_number, user_email, total_price)
    VALUES('F-2025-1', 'scofield@gmail.com', 106000);

INSERT INTO invoices(invoice_number, user_email, total_price)
    VALUES('F-2025-2', 'armando@yahoo.com', 52000);

INSERT INTO invoices(invoice_number, user_email, total_price)
    VALUES('F-2025-3', 'armando@yahoo.com', 82000);

INSERT INTO invoices(invoice_number, user_email, total_price)
    VALUES('F-2025-4', 'armando@yahoo.com', 20000);

INSERT INTO invoices(invoice_number, user_email, total_price)
    VALUES('F-2025-5', 'scofield@gmail.com', 40000);



-- junction products/invoices table
INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 70000, 1, 1);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 20000, 2, 1);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(2, 16000, 3, 1);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(2, 40000, 2, 2);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 8000, 3, 2);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 70000, 1, 3);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 12000, 4, 3);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(1, 20000, 2, 4);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(2, 16000, 3, 5);

INSERT INTO products_invoices(total_products, purchase_amount, product_id, invoice_id)
    VALUES(2, 24000, 4, 5);


-- carts table
INSERT INTO carts(user_email)
    VALUES('scofield@gmail.com');

INSERT INTO carts(user_email)
    VALUES('armando@yahoo.com');


-- junction products/carts table
INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 1);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 2);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 3);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 3);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 3);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 3);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 4);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(1, 4);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 1);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 2);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 2);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 2);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 3);

INSERT INTO products_carts(cart_id, product_id)
    VALUES(2, 4);