from flask import Blueprint, request, jsonify
from repos.invoices_repository import InvoicesRepository
from validators.invoices_validators import InvoiceValidators
from exceptions.generated_exceptions import InvoiceNotFoundError, ValidationError
from routes.utils_routes import admin_only
from db.tables import engine
from auth.jwt_instance import jwt_manager

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
  


@invoice_bp.route('/check-invoices', methods=['GET'])
def check_invoices():

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

    invoices_list = invoice_repo.check_invoices(user_id)
    return jsonify(invoices_list), 200
  except Exception as e:
    return jsonify({"error": str(e)})