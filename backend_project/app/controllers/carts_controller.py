from flask import request, jsonify, g
from app.db.database import engine
from app.exceptions.exceptions import ValidationError, NotFoundError
from app.services.cart_services import CartServices
from app.repos.carts_repository import CartsRepository
from app.validators.carts_validators import CartsValidator

carts_validator = CartsValidator()
carts_repo = CartsRepository(engine)
cart_services = CartServices(carts_validator, carts_repo)

class CartsController:

  def get_carts(self):
    try:
      params = request.args.to_dict()
      return cart_services.list_carts(params)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 


  def post_cart(self):
    data = request.get_json()

    try:
      cart_services.add_product_to_cart(g.user_id, data)
      return jsonify({"success": "Products added to the cart"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def update_by_admin(self, id):
    try:
      data = request.get_json()
      cart_services.update_cart_by_admin(id, data)
      return jsonify({"message": "cart successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except ValueError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def update_carts_items(self):
    try:
      data = request.get_json()
      cart_services.update_cart_products(g.user_id, data)
      return jsonify({"message": "cart successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except ValueError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def checkout_cart(self):
    data = request.get_json()

    try:
      cart_services.checkout_cart(g.user_id, data)
      return jsonify({"success": "invoice created"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500