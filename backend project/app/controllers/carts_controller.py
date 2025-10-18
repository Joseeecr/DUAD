from flask import request, jsonify, g
from db.database import engine
from exceptions.exceptions import ValidationError, NotFoundError
from services.cart_services import CartServices
from repos.carts_repository import CartsRepository
from validators.carts_validators import CartsValidator
from auth.admin_only import admin_only
from controllers.controllers_utils import jwt_required

carts_validator = CartsValidator()
carts_repo = CartsRepository(engine)
cart_services = CartServices(carts_validator, carts_repo)


class CartsController:

  @admin_only
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


  @jwt_required
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


  @admin_only
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
    

  @jwt_required
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


  @jwt_required
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