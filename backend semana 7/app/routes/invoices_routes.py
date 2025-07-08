from flask import Blueprint, request, jsonify
from repos.invoices_repository import InvoicesRepository
from validators.invoices_validators import InvoiceValidators
from exceptions.generated_exceptions import InvoiceNotFoundError, ValidationError
from routes.utils_routes import admin_only
from db.tables import engine

invoice_validator = InvoiceValidators()
invoice_repo = InvoicesRepository(engine, invoice_validator)
invoice_bp = Blueprint('invoice', __name__, url_prefix='/invoices')


@invoice_bp.route('/', methods=['GET'])
@admin_only
def list_invoices():
  raw_params = request.args.to_dict()

  try:
    filters = invoice_validator.validate_invoice_filters(raw_params)
    invoices = invoice_repo.get_invoices(filters)
    return jsonify(invoices), 200

  except ValidationError as e:
    return jsonify({"error": str(e)}), 400
  except InvoiceNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  


@invoice_bp.route('/<int:user_id>', methods=['GET'])
def list_invoices_by_user_id(user_id):

  try:
    invoices = invoice_repo.get_invoice_by_user_id(user_id)
    return jsonify(invoices), 200

  except InvoiceNotFoundError as e:
    return jsonify({"error": str(e)}), 404
  except Exception as e:
    return jsonify({"error": str(e)}), 500