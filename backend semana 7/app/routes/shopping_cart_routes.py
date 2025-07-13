from flask import Blueprint, request, Response, jsonify
from repos.shopping_cart_repository import ShoppingCartRepository
from validators.shopping_cart_validators import ShoppingCartValidators
from exceptions.generated_exceptions import ValidationError, CartNotFoundError, ColumnNotFoundError, ProductNotFoundError
from db.tables import engine
from routes.utils_routes import admin_only 
from auth.jwt_instance import jwt_manager

shopping_cart_validator = ShoppingCartValidators()
shopping_cart_repo = ShoppingCartRepository(engine, shopping_cart_validator)
shopping_cart_bp = Blueprint('carts', __name__, url_prefix='/carts')


@shopping_cart_bp.route('/', methods=['GET'])
@admin_only
def list_carts():
  raw_params = request.args.to_dict()

  try:
    filters = shopping_cart_validator.validate_cart_filters(raw_params)
    carts = shopping_cart_repo.get_carts(filters)
    return jsonify(carts), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except CartNotFoundError as e:
    return jsonify({"error": str(e)}), 404


@shopping_cart_bp.route('/items', methods=['POST'])
def add_item_to_cart():

  token = request.headers.get('Authorization')

  if token is None:
    return jsonify({"error": "Authorization token missing"}), 401

  raw_token = token.replace("Bearer ","")
  data = request.get_json()
  product_id = data.get('product_id')
  quantity = data.get('quantity')

  try:

    decoded = jwt_manager.decode(raw_token)
    if "id" in decoded:
      user_id = decoded["id"]

    else:
      return jsonify({"error": "id field missing"}), 401


    shopping_cart_repo.add_product_to_cart(user_id, product_id, quantity)
    return jsonify({"message": "Product added to cart"}), 201
  
  except ProductNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  
  except Exception as e:
    return jsonify({"error": str(e)}), 401


@shopping_cart_bp.route('/update/<int:_id>', methods=['PATCH'])
@admin_only
def update(_id):
  try:
    data = request.get_json()
    shopping_cart_repo.update_cart(_id, data)
    return jsonify("Cart successfully updated"), 200
  except ColumnNotFoundError as e:
    return jsonify({"error": str(e)}), 400


@shopping_cart_bp.route('/delete/<int:_id>', methods=['DELETE'])
@admin_only
def delete(_id):
  success = shopping_cart_repo.delete_cart(_id)

  if not success:
    return Response(f"Cart with id '{_id}' not found", status=404)

  return Response("Resource deleted successfully", status=200)


@shopping_cart_bp.route('/checkout', methods=['POST'])
def checkout():
  token = request.headers.get('Authorization')

  if token is None:
    return jsonify({"error": "Authorization token missing"}), 401

  raw_token = token.replace("Bearer ","")

  try:

    decoded = jwt_manager.decode(raw_token)
    if "id" in decoded:
      user_id = decoded["id"]

    else:
      return jsonify({"error": "id field missing"}), 401


    shopping_cart_repo.checkout_cart(user_id)
    return jsonify({"Success": "Cart successfully closed"}), 201
  
  except CartNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  
  except Exception as e:
    return jsonify({"error": str(e)}), 401