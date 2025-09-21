from flask import request, jsonify, g
from app.exceptions.exceptions import ValidationError, NotFoundError

class CartsController:
  def __init__(self, cart_services):
    self.cart_services = cart_services

  def get_carts(self):
    try:
      params = request.args.to_dict()
      carts = self.cart_services.list_carts(params)
      return jsonify(carts), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500


  def post_cart(self):
    data = request.get_json()

    try:
      self.cart_services.add_product_to_cart(g.user_id, data)
      return jsonify({"success": "Products added to the cart"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500


  def update_by_admin(self, id):
    try:
      data = request.get_json()
      self.cart_services.update_cart_by_admin(id, data)
      return jsonify({"message": "cart successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500


  def update_carts_items(self):
    try:
      data = request.get_json()
      self.cart_services.update_cart_products(g.user_id, data)
      return jsonify({"message": "cart successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500


  def checkout_cart(self):
    data = request.get_json()

    try:
      self.cart_services.checkout_cart(g.user_id, data)
      return jsonify({"success": "invoice created"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500
