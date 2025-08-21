from flask import Blueprint, request, Response, jsonify
from repos.products_repository import ProductsRepository
from validators.products_validators import ProductValidators
from exceptions.generated_exceptions import ProductNotFoundError, ValidationError, ColumnNotFoundError
from db.tables import engine
from routes.utils_routes import admin_only
from cache.cache_manager_instance import cache_manager

product_validator = ProductValidators()
product_repo = ProductsRepository(engine, product_validator)
product_bp = Blueprint('fruit', __name__, url_prefix='/fruits')


@product_bp.route('/', methods=['GET'])
@admin_only
def list_products():
  raw_params = request.args.to_dict()
  try:
    filters = product_validator.validate_product_filters(raw_params)
    cache_key = cache_manager.make_cache_key("fruits:all", filters)

    cached =  cache_manager.get_data(cache_key)

    if cached:
      return jsonify(cached), 200

    products = product_repo.get_products(filters)
    cache_manager.store_data(cache_key, products)
    return jsonify(products), 200

  except ProductNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  except Exception as e:
    return jsonify({"error": str(e)}), 500


@product_bp.route('/<int:id>', methods=['GET'])
@admin_only
def get_product_id(id):
  cache_key = f"fruits:{id}"
  try:
    cached =  cache_manager.get_data(cache_key)

    if cached:
      return jsonify(cached), 200

    product = product_repo.get_product_by_id(id)
    cache_manager.store_data(cache_key, product, time_to_live=600)
    return jsonify(product), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except ProductNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  except Exception as e:
    return jsonify({"error": str(e)}), 500


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
    cache_manager.delete_data_with_pattern("fruits:all*")
    return {"success": "product was successfully inserted"}, 200

  else:
    return {"error": "that product is already in the DB"}, 400


@product_bp.route('/update/<int:_id>', methods=['PATCH'])
@admin_only
def update(_id):
  try:
    data = request.get_json()
    product_repo.update_product(_id, data)
    cache_manager.delete_data(f"fruits:{_id}")
    cache_manager.delete_data_with_pattern(f"fruits:all*")
    return jsonify("Product successfully updated"), 200
  except ProductNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  except ColumnNotFoundError as e:
    return jsonify({"error": str(e)}), 404


@product_bp.route('/delete/<int:_id>', methods=['DELETE'])
@admin_only
def delete(_id):
  success = product_repo.delete_product(_id)

  if not success:
    return Response("Product not found", status=404)

  cache_manager.delete_data(f"fruits:{_id}")
  cache_manager.delete_data_with_pattern(f"fruits:all*")
  return Response("Resource deleted successfully", status=200)