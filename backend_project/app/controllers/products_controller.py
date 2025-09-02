from flask import request, jsonify
from db.database import engine
from exceptions.exceptions import ValidationError, NotFoundError
from services.products_services import ProductsService
from repos.products_repository import ProductsRepository
from validators.products_validators import ProductsValidator



products_validator = ProductsValidator()
products_repo = ProductsRepository(engine)
products_service = ProductsService(products_validator, products_repo)


class ProductsController:

  def get_products(self):
    try:
      params = request.args.to_dict()
      products = products_service.list_products(params)
      return jsonify(products), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 


  def get_product_id(self, id):
    try:
      
      product = products_service.get_product_by_id(id)
      return jsonify(product), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def post_product(self):
    try:

      data = request.get_json()
      products_service.insert_product(data)
      return jsonify({"success": "new product added"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def update_by_admin(self, id):
    try:
      data = request.get_json()
      products_service.update_product_by_admin(id, data)
      return jsonify({"message": "product successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except ValueError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500


  def delete_product(self, id):
    try:
      products_service.delete_product(id)
      return jsonify(), 204
    except ValueError as e:
      return jsonify({"error": str(e)}), 404