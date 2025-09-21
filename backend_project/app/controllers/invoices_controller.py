from flask import request, jsonify, g
from app.exceptions.exceptions import ValidationError, NotFoundError


class InvoicesController:
  def __init__(self, invoices_service):
    self.invoices_service = invoices_service

  def get_invoices(self):
    try:

      params = request.args.to_dict()
      return self.invoices_service.list_invoices(params)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500

  def check_user_invoices(self):
    try:
      return self.invoices_service.get_user_invoices(g.user_id)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500