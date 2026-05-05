# API Documentation

This project provides an API for managing **Users**, **Products**, **Carts**, and **Invoices**.  
Most endpoints require authentication via tokens, and some require admin privileges.

---

## Users

GET /users
### Get all users
- URL: `http://localhost:5000/users`  
- Requires **admin token**  
- Supports query parameters  

---
GET /users/me
### Get current user
- URL: `http://localhost:5000/users/me`  
- Requires **user token**  
- Returns decoded token information  

---

### Register a new user
POST /users/register
- URL: `http://localhost:5000/users/register`  
- Accepts JSON payload  
- Adds user to the database and returns a token  

**Payload example:**
```json
{
    "name": "John",
    "last_name": "Doe",
    "email": "johndoe@email.com",
    "password": "mypassword",
    "phone_number": "123456789",
    "is_admin": false
}

Login
POST /users/login
- URL: http://localhost:5000/users/login
- Accepts JSON payload
- Returns a token if credentials are valid

Payload example:
{
    "email": "johndoe@email.com",
    "password": "mypassword"
}

Delete user
DELETE /users/delete/{id}
- URL: http://localhost:5000/users/delete/13
- Deletes a user by ID

### Update user
PATCH /users/update/{id}
- URL: http://localhost:5000/users/update/8
- Accepts JSON payload with fields to update
- Requires admin token

---

## Products

### Get all products
GET /products
- URL: http://localhost:5000/products
- Requires admin token
- Supports query parameters

### Create new product
POST /products
- URL: http://localhost:5000/products
- Accepts JSON payload
- Adds product to the database

Payload example:
{
    "name": "Dog Chew Bone",
    "price": 2.50,
    "sku": "ABCD1234",
    "stock": "5",
    "category_id": 7
}

### Update product
PATCH /products/update/{id}
- URL: http://localhost:5000/products/update/1
- Accepts JSON payload with fields to update

Payload example:
{
    "stock": 15
}

### Delete product
DELETE /products/delete/{id}
- URL: http://localhost:5000/products/delete/2
- Deletes product by ID

---

## Carts

### Get all carts
GET /carts
- URL: http://localhost:5000/carts
- Requires admin token
- Supports query parameters

### Add product to cart
POST /carts/add
- URL: http://localhost:5000/carts/add
- Requires user token
- Accepts JSON payload

Payload example:
{
    "product_id": 10,
    "quantity": 1
}

### Checkout
POST /carts/checkout
- URL: http://localhost:5000/carts/checkout
- Requires user token
- Creates invoice and associates shipping address

Payload example:
{
    "payment_method": "sinpe",
    "shipping_address": {
        "street": "Calle 0, Avenida Central",
        "city": "San José",
        "province": "San José",
        "zip_code": "10101",
        "country": "Costa Rica"
    }
}

### Update cart
PATCH /carts/update/{cart_id}
- URL: http://localhost:5000/carts/update/1
- Requires admin token
- Accepts JSON payload

Payload example:
{
    "status": "active"
}

### Update cart items
PATCH /update-carts-items
- URL: http://localhost:5000/update-carts-items/
- Updates items in cart_products table
- Requires product ID in payload

Payload example:
{
    "quantity": 1,
    "product_id": 1
}

---

## Invoices

### Get all invoices
GET /invoices
- URL: http://localhost:5000/invoices
- Requires user token
- Supports query parameters

### Get invoices by user
GET /invoices/{user_id}
- URL: http://localhost:5000/invoices/9
- Requires user token
- Returns all invoices for a specific user



To run the tests, execute the following command from the project root (`backend_project`):
"python -m run_tests"

This will generate a short report with the test results.

To run this project, first install all dependencies listed in the requirements.txt file.  
You will also need to generate a private key for the authentication module and create a .env file containing the database URI.  
The variable in the .env file must be named "DATABASE_URL".
