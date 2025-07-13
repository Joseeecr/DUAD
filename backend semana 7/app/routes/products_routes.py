from flask import Blueprint, request, Response, jsonify
from repos.products_repository import ProductsRepository
from validators.products_validators import ProductValidators
from exceptions.generated_exceptions import ProductNotFoundError, ValidationError, ColumnNotFoundError
from db.tables import engine
from routes.utils_routes import admin_only

product_validator = ProductValidators()
product_repo = ProductsRepository(engine, product_validator)
product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
@admin_only
def list_products():
  raw_params = request.args.to_dict()

  try:
    filters = product_validator.validate_product_filters(raw_params)
    products = product_repo.get_products(filters)
    return jsonify(products), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except ProductNotFoundError as e:
    return jsonify({"error": str(e)}), 404



@product_bp.route('/', methods=['POST'])
@admin_only
def add_product():
  data = request.get_json()

  name = data.get("name")
  price = data.get("price")
  quantity = data.get("quantity")
  errors = product_validator.insert_product_validator(data)
  
  if errors:
    return {"errors": errors}, 400

  elif product_repo.insert_product(name=name, price=price, quantity=quantity):
    return {"success": "product was successfully inserted"}, 200

  else:
    return {"error": "that product is already in the DB"}, 400


@product_bp.route('/update/<int:_id>', methods=['PATCH'])
@admin_only
def update(_id):
  try:
    data = request.get_json()
    product_repo.update_product(_id, data)
    return jsonify("Product successfully updated"), 200
  except ColumnNotFoundError as e:
    return jsonify({"error": str(e)}), 400


@product_bp.route('/delete/<int:_id>', methods=['DELETE'])
@admin_only
def delete(_id):
  success = product_repo.delete_product(_id)

  if not success:
    return Response("Product not found", status=404)

  return Response("Resource deleted successfully", status=200)