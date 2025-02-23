def cart_validator(carts, cart_id):
    cart = next((c for c in carts if c["cart_id"] == cart_id), None)

    if not cart:
        return {"error": "Cart Not found"}
    return cart


def product_validator(products, product_id):
    product_to_add = next((p for p in products if p["product_id"] == product_id), None)

    if not product_to_add:
        return {"error": "Product Not Found"}
    return product_to_add


def existing_product_validator(cart, product_id):
    existing_product = next((p for p in cart["products"] if p["product_id"] == product_id), None)
    return existing_product