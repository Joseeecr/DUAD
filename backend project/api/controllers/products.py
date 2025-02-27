from services.json_manager  import read_json_file, write_json_file
from validators.validators import validate_id, validate_title #,validate_status, validate_prize
from flask import request

def add_products():
    products = read_json_file("products.json")

    try:
        new_product = {
                    "product_id": request.json["product_id"],
                    "title": request.json["title"],
                    "prize": request.json["prize"],
                    "brand": request.json["brand"],
                    "stock": request.json["stock"],
        }
    except KeyError as ex:
        return f"Missing field: {ex.args[0]}", 400

    # errors = [
    #     validate_id(new_product, products),
    #     validate_title(new_product["title"]),
    #     validate_prize(new_product["prize"]),
    #     validate_status(new_product["brand"]),
    # ]
    
    # errors= [error for error in errors if error]
    # if errors:
    #     return {"errors": errors}, 400

    products.append(new_product)

    write_json_file("products.json", products)

    return new_product


def get_products():
    products = read_json_file("products.json")
    filtered_product = products
    brand_filter = request.args.get("brand")
    product_id_filter = request.args.get("product_id")

    if product_id_filter is not None:
        product_id_filter = int(product_id_filter)

    if brand_filter or product_id_filter:
        filtered_product = list(
            filter(lambda product: product["brand"] == brand_filter or product["product_id"] == product_id_filter, filtered_product)
            )

    return {"data": filtered_product}


def delete_product(product_id):
    products = read_json_file("products.json")

    for product in products:
        if product["product_id"] == product_id:
            products.remove(product)
        
            write_json_file("products.json", products)

            return "Product succesfully deleted"

    return "Product not found", 404


def edit_product(product_id, update_data):
    products = read_json_file("products.json")
    product_to_modify = None

    for product in products:
        if product["product_id"] == product_id:
            product_to_modify = product
            break

    if product_to_modify is None:
        return "Product not found", 404

    # errors = []
    # for key in update_data.keys():
    #     if key in product_to_modify:
    #         if key == "id":
    #             error = validate_id(update_data, products)
    #         elif key == "title":
    #             error = validate_title(update_data["title"])
    #         # elif key == "prize":
    #         #     error = validate_prize(update_data["prize"])
    #         # elif key == "status":
    #         #     error = validate_status(update_data["status"])

    #         if error:
    #             errors.append({key : error})

    # if errors:
    #     return {"errors": errors}, 400

    for key, value in update_data.items():
        if key in product_to_modify:
            product_to_modify[key] = value

    write_json_file("products.json", products)

    return "Product succesfully updated"