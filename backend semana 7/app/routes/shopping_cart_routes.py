from flask import Blueprint, request, Response, jsonify
from repos.shopping_cart_repository import ShoppingCartRepository
from validators.shopping_cart_validators import ShoppingCartValidators
from exceptions.generated_exceptions import UserNotFoundError, ValidationError, CartNotFoundError, ColumnNotFoundError, ProductNotFoundError
from db.tables import engine
from routes.utils_routes import admin_only 

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



@shopping_cart_bp.route('/', methods=['POST'])
@admin_only
def add_cart():
  data = request.get_json()
  user_id = data.get("user_id")
  errors = shopping_cart_validator.create_cart_registration(data)
  
  if errors:
    return {"errors": errors}, 400

  try: 
    shopping_cart_repo.insert_cart(user_id=user_id)
    return jsonify("Cart was succesfully added"), 200

  except UserNotFoundError as e:
    return jsonify({"error": str(e)}), 400


@shopping_cart_bp.route('/<int:shopping_cart_id>/items', methods=['POST'])
@admin_only
def add_item_to_cart(shopping_cart_id):
  data = request.get_json()
  product_id = data.get('product_id')
  quantity = data.get('quantity')

  try:
    shopping_cart_repo.add_product_to_cart(shopping_cart_id, product_id, quantity)
    return jsonify({"message": "Product added to cart"}), 201
  
  except CartNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  
  except ProductNotFoundError as e:
      return jsonify({"error": str(e)}), 404


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


@shopping_cart_bp.route('/<int:shopping_cart_id>/close', methods=['POST'])
def close_cart(shopping_cart_id):
  try:
    shopping_cart_repo.close_cart(shopping_cart_id)
    return jsonify({"message": "Cart closed successfully"}), 200
  except CartNotFoundError as e:
      return jsonify({"error": str(e)}), 404
  except Exception as e:
      return jsonify({"error": str(e)}), 400
