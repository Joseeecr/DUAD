from flask import Flask
from routes.user_routes import user_bp
from routes.products_routes import product_bp
from routes.shopping_cart_routes import shopping_cart_bp
from routes.invoices_routes import invoice_bp
from routes.roles_routes import role_bp


app = Flask("user-service")
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(shopping_cart_bp)
app.register_blueprint(invoice_bp)
app.register_blueprint(role_bp)

if __name__ == "__main__":
  app.run(host="localhost", debug=True)