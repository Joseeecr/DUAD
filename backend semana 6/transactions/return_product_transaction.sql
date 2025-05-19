SET search_path TO transactions_practice;

DO $$

BEGIN

--1 verify that the invoice exists
IF NOT EXISTS (
SELECT 1
FROM invoices
WHERE id = 1
  AND status = 'Completed'
) THEN
  RAISE NOTICE 'Invoice does not exist or status is already returned';
  RETURN;
END IF;

--2 update stock
UPDATE products
SET stock = stock + invoices.quantity
FROM invoices
WHERE invoices.product_id = products.id
  AND invoices.id = 1;

--3 set the invoice status as 'returned'
UPDATE invoices
SET status = 'returned'
WHERE id = 1;

END;
$$ LANGUAGE plpgsql;