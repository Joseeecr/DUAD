from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


class AuthAPI(MethodView):
    pass


class ProductAPI(MethodView):
    pass


class CartAPI(MethodView):
    pass


class SalesAPI(MethodView):
    pass


class InvoiceAPI(MethodView):
    pass

#Auth
auth_view = AuthAPI.as_view('auth_api')
app.add_url_rule('/auth/register', view_func=auth_view, methods=['POST'])
app.add_url_rule('/auth/login', view_func=auth_view, methods=['POST'])
app.add_url_rule('/auth/logout', view_func=auth_view, methods=['POST'])

#products
product_view = ProductAPI.as_view('product_api')
app.add_url_rule('/products/', view_func=product_view, methods=['GET', 'POST'])
app.add_url_rule('/products/<string:slug>', view_func=product_view, methods=['GET', 'PUT', 'DELETE'])

#carts
cart_view = CartAPI.as_view('cart_api')
app.add_url_rule('/cart/', view_func=cart_view, methods=['POST'])
app.add_url_rule('/cart/<string:slug>', view_func=cart_view, methods=['GET'])
app.add_url_rule('/cart/<string:slug>/add', view_func=cart_view, methods=['PUT'])
app.add_url_rule('/cart/<string:slug>/remove', view_func=cart_view, methods=['PUT'])

#sales
sales_view = SalesAPI.as_view('sales_api')
app.add_url_rule('/sales/', view_func=sales_view, methods=['POST'])
app.add_url_rule('/sales/<string:slug>', view_func=sales_view, methods=['GET'])

#invoices
invoice_view = InvoiceAPI.as_view('invoice_api')
app.add_url_rule('/invoices/<int:invoice_number>', view_func=invoice_view, methods=['GET'])
app.add_url_rule('/invoices/<int:invoice_number>/refund', view_func=invoice_view, methods=['POST'])

