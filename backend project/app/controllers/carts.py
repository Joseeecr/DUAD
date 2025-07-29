# from validators.cart_validators import cart_validator, product_validator, existing_product_validator
# from flask import request

# def create_cart(user_id):
#     carts = read_json_file("carts.json")

#     new_cart = {
#         "cart_id": len(carts) + 1,
#         "user_id": user_id,
#         "products": [],
#         "status": "active"
#     }

#     carts.append(new_cart)

#     write_json_file("carts.json", carts)

#     return new_cart


# def get_carts():
#     carts = read_json_file("carts.json")

#     filtered_cart = carts
#     cart_id_filter = request.args.get("cart_id")

#     if cart_id_filter is not None:
#         cart_id_filter = int(cart_id_filter)

#     if cart_id_filter:
#         filtered_cart = list(
#             filter(lambda cart: cart["cart_id"] == cart_id_filter, filtered_cart)
#             )

#     return {"data": filtered_cart}


# def add_products_to_cart(cart_id):
#     carts = read_json_file("carts.json")
#     products = read_json_file("products.json")

#     cart = cart_validator(carts, cart_id)
#     if "error" in cart:
#         return cart, 404  

#     data = request.get_json()
#     product_id = data.get("product_id")

#     if not product_id:
#         return {"error": "Missing product_id"}, 400

#     product_to_add = product_validator(products, product_id)
#     if "error" in product_to_add:
#         return product_to_add, 404

#     if product_to_add["stock"] <= 0:
#         return {"error": "Out of stock"}, 400

#     product_to_add["stock"] -= 1
#     write_json_file("products.json", products)

#     existing_product = existing_product_validator(cart, product_id)

#     if existing_product:
#         existing_product["amount"] += 1

#     else:
#         cart["products"].append({
#             "product_id": product_to_add["product_id"],
#             "title": product_to_add["title"],
#             "prize": product_to_add["prize"],
#             "brand": product_to_add["brand"],
#             "amount": 1
#         })

#     write_json_file("carts.json", carts)

#     return {
#         "message": "Product added to cart succesfully", 
#         "cart": cart
#     }


# def modify_amount_of_products(cart_id, product_id):
#     carts = read_json_file("carts.json")
#     products = read_json_file("products.json")

#     cart = cart_validator(carts, cart_id)
#     if "error" in cart:
#         return cart, 404 

#     product = product_validator(products, product_id)
#     if "error" in product:
#         return product, 404

#     existing_product = existing_product_validator(cart, product_id)
#     if not existing_product:
#         return  {"error": "Product Not found"}, 404

#     data = request.get_json()
#     new_amount = data.get("amount")

#     if not isinstance(new_amount, int) or new_amount < 0:
#         return {"error": "'amount' should be a positive number"}, 400

#     previous_amount = existing_product["amount"]
#     difference = new_amount - previous_amount

#     if difference > 0:
#         if product["stock"] < difference:
#             return {"error": "Not enough stock available", "Current_stock": product["stock"]}, 400
#         product["stock"] -= difference

#     elif difference < 0:
#         product["stock"] -= difference

#     if new_amount == 0:
#         cart["products"].remove(existing_product)
#     else:
#         existing_product["amount"] = new_amount

#     write_json_file("products.json", products)
#     write_json_file("carts.json", carts)

#     return {"message": "Product amount updated", "new_amount": new_amount, "Current_Stock": product["stock"]}


# def delete_cart(cart_id):
#     carts = read_json_file("carts.json")
#     products = read_json_file("products.json")

#     cart_to_delete = cart_validator(carts, cart_id)
#     if "error" in cart_to_delete:
#         return cart_to_delete, 404
    
#     for item in cart_to_delete["products"]:
#         product = product_validator(products, item["product_id"])
#         if product:
#             product["stock"] += item["amount"]

#     carts = [cart for cart in carts if cart["cart_id"] != cart_id]

#     write_json_file("carts.json", carts)
#     write_json_file("products.json", products)

#     return {"message": "Cart successfully deleted"}