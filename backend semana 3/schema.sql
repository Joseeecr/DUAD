CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code CHAR(8) UNIQUE NOT NULL,
    product_name VARCHAR(10) NOT NULL,
    price INT NOT NULL,
    pub_date DATE NOT NULL,
    brand VARCHAR(10)
); 

CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number CHAR(10) NOT NULL,
    purchase_date DATE DEFAULT (DATE('now')),
    user_email CHAR(25) NOT NULL,
    total_price INT NOT NULL
);

CREATE TABLE products_invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_products SMALLINT NOT NULL,
    purchase_amount INT NOT NULL,
    product_id INT REFERENCES products(id) NOT NULL,
    invoice_id INT REFERENCES invoices(id) NOT NULL
);

CREATE TABLE carts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email CHAR(25) NOT NULL,
    created_date DATE DEFAULT (DATE('now')),
    expiration_date DATE DEFAULT (DATE('now'))
);

CREATE TABLE products_carts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INT REFERENCES carts(id),
    product_id INT REFERENCES products(id)
);