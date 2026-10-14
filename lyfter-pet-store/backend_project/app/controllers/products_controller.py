from flask import request, jsonify
from app.exceptions.exceptions import ValidationError, NotFoundError
import logging
logger = logging.getLogger(__name__)

class ProductsController:
  def __init__(self, products_service):
    self.products_service = products_service

  def get_products(self):
    try:
      params = request.args.to_dict()
      if "category_id" in request.args:
        params["category_id"] = request.args.getlist("category_id")

      products = self.products_service.list_products(params)
      return jsonify(products), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      logger.exception("Error when getting the products")
      return jsonify({"error": "Internal server error"}), 500


  def get_product_id(self, id):
    try:
      
      product = self.products_service.get_product_by_id(id)
      return jsonify(product), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception:
      logger.exception("Error when getting individual product")
      return jsonify({"error": "Internal server error"}), 500


  def post_product(self):
    try:

      data = request.get_json()
      self.products_service.insert_product(data)
      return jsonify({"success": "new product added"}), 201

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except Exception:
      logger.exception("Error while adding products")
      return jsonify({"error": "Internal server error"}), 500


  def update_by_admin(self, id):
    try:
      data = request.get_json()
      self.products_service.update_product_by_admin(id, data)
      return jsonify({"message": "product successfully updated"}), 200
    except ValidationError as e:
      return jsonify({"error": str(e)}), 422
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception:
      logger.exception("Error while updating product")
      return jsonify({"error": "Internal server error"}), 500


  def delete_product(self, id):
    try:
      self.products_service.delete_product(id)
      return jsonify(), 204
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception:
      logger.exception("Error while deleting product")
      return jsonify({"error": "Internal server error"}), 500