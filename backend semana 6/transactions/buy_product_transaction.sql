SET search_path TO transactions_practice;

DO $$
DECLARE
  v_invoice_id INTEGER;

BEGIN

--1 verify product's stock
IF NOT EXISTS (
SELECT 1
FROM products
WHERE id = 1
  AND stock > 0
) THEN
  RAISE NOTICE 'Insufficient stock';
  RETURN;
END IF;

--2 verify that user exists
IF NOT EXISTS (
SELECT 1
FROM users
WHERE id = 1
) THEN
  RAISE NOTICE 'User does not exist';
  RETURN;
END IF;

--3 create the invoice
INSERT INTO invoices(user_id, product_id, total, status, quantity)
VALUES(1, 3, 6.00, 'Completed', 1)
RETURNING id INTO v_invoice_id;


--4 Update stock
UPDATE products
SET stock = stock - invoices.quantity
FROM invoices
WHERE invoices.id = v_invoice_id
  AND invoices.product_id = products.id;

END;
$$ LANGUAGE plpgsql;