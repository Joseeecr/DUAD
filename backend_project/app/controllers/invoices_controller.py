from flask import request, jsonify, g
from app.exceptions.exceptions import ValidationError, NotFoundError


class InvoicesController:
  def __init__(self, invoices_service):
    self.invoices_service = invoices_service

  def get_invoices(self):
    try:

      params = request.args.to_dict()
      invoices = self.invoices_service.list_invoices(params)
      return jsonify(invoices), 200

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500

  def check_user_invoices(self):
    try:
      invoices = self.invoices_service.get_user_invoices(g.user_id)
      return jsonify(invoices), 200

    except NotFoundError as e:
      return jsonify({"error": str(e)}), 404
    except Exception as e:
      print({"error": str(e)})
      return jsonify({"error": "Internal Server Error"}), 500