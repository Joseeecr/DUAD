from flask import Flask, request, jsonify
from flask.views import MethodView
from controllers.products import add_products, get_products, edit_product, delete_product
from controllers.carts import create_cart, get_carts, add_products_to_cart, delete_cart, modify_amount_of_products
from controllers.sales import checkout_cart
from controllers.invoices import get_invoice, refund_invoice

app = Flask(__name__)

class AuthAPI(MethodView):
    pass


class ProductAPI(MethodView):

    def get(self):
        _get_products = get_products()
        return _get_products


    def post(self):
        _add_products = add_products()
        return _add_products


    def put(self, product_id):
        update_data = request.json

        result = edit_product(product_id, update_data)

        return result


    def delete(self, product_id):
        _delete_product = delete_product(product_id)

        return _delete_product


class CartAPI(MethodView):

    def post(self):
            data = request.get_json(silent=True)

            if data is None:
                return jsonify({"error": "Invalid JSON or empty request body"}), 400

            if "user_id" not in data:
                return jsonify({"error": "Missing field: user_id"}), 400

            new_cart = create_cart(data["user_id"])

            return jsonify(new_cart), 201


    def get(self):

        _get_carts = get_carts()

        return _get_carts


    def put(self, cart_id):

        add_product = add_products_to_cart(cart_id)


        return add_product


    def patch(self, cart_id, product_id):
        _modify_amount = modify_amount_of_products(cart_id, product_id)

        return _modify_amount


    def delete(self, cart_id):

        _delete_cart = delete_cart(cart_id)

        return _delete_cart

class SalesAPI(MethodView):
    def post(self, cart_id):
        _checkout_cart = checkout_cart(cart_id)

        return _checkout_cart


class InvoiceAPI(MethodView):

    def get(self, invoice_number):
        _get_invoice = get_invoice(invoice_number)
        return _get_invoice


    def post(self, invoice_number):
        _refund_invoice = refund_invoice(invoice_number)

        return _refund_invoice



#Auth
auth_view = AuthAPI.as_view("auth_api")
app.add_url_rule("/auth/register", view_func=auth_view, methods=["POST"])
app.add_url_rule("/auth/login", view_func=auth_view, methods=["POST"])
app.add_url_rule("/auth/logout", view_func=auth_view, methods=["POST"])

#products
product_view = ProductAPI.as_view("product_api")
app.add_url_rule("/products/", view_func=product_view, methods=["GET", "POST"])
app.add_url_rule("/products/<int:product_id>", view_func=product_view, methods=["PUT", "DELETE"])

#carts
cart_view = CartAPI.as_view("cart_api")
app.add_url_rule("/carts/", view_func=cart_view, methods=["POST", "GET"])  # create cart/get cart
app.add_url_rule("/carts/<int:cart_id>", view_func=cart_view, methods=["PUT", "DELETE"]) # update(add products to cart)/delete cart
app.add_url_rule("/carts/<int:cart_id>/<int:product_id>/update", view_func=cart_view, methods=["PATCH"])  # modify amount of products, if amount ==0 removes product from cart


#sales
sales_view = SalesAPI.as_view("sales_api")
app.add_url_rule("/sales/<int:cart_id>/checkout", view_func=sales_view, methods=["POST"])  # finalize purchase

#invoices
invoice_view = InvoiceAPI.as_view("invoice_api")
app.add_url_rule("/invoices/<path:invoice_number>", view_func=invoice_view, methods=["GET"])
app.add_url_rule("/invoices/<path:invoice_number>/refund", view_func=invoice_view, methods=["POST"])

if __name__ == "__main__":
    app.run(host="localhost", debug=True)