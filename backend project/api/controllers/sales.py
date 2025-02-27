from services.json_manager import read_json_file, write_json_file
from validators.cart_validators import cart_validator
from flask import request
from random import randint
import datetime

def checkout_cart(cart_id):
    carts = read_json_file("carts.json")
    sales = read_json_file("invoices.json")

    try:
        new_sale = {
                    "user_email": request.json["user_email"],
                    "address": request.json["address"],
                    "payment_method": request.json["payment_method"],
                    "phone_number" : request.json["phone_number"],
        }

    except KeyError as ex:
        return f"Missing field: {ex.args[0]}", 400

    cart = cart_validator(carts, cart_id)
    if "error" in cart:
        return cart, 404

    if not cart["products"]:
        return {
            "mesagge":"Cart has no products",
            "message": "If you want to finalize a purchase, add some products"
        }, 400

    total_prize = []
    for item in cart["products"]:
        item["prize"] = int(item["prize"].replace('$', ''))
        total_prize.append(item["prize"] * item["amount"])

    total_prize = sum(total_prize)
    invoice_number = hex(randint(0, 100000))
    current_date = datetime.datetime.now()
    formated_date = current_date.strftime("%x")

    new_sale.update({
        "invoice_number": invoice_number,
        "total_prize": f"${total_prize}",
        "date": formated_date,
        "products": cart["products"]
    })

    sales.append(new_sale)

    carts.remove(cart)
    write_json_file("carts.json", carts)
    write_json_file("invoices.json", sales)

    return new_sale