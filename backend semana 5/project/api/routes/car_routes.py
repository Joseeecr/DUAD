from flask import Blueprint
from api.views.car_view import CarAPI

class CarBlueprint:
  def __init__(self, car_handler):
    self.car_handler = car_handler
    self.blueprint = Blueprint('cars', __name__)
    self._register_routes()


  def _register_routes(self):
    car_view = CarAPI.as_view('car_api', car_handler=self.car_handler)

    self.blueprint.add_url_rule('/cars', view_func=car_view, methods=['GET', 'POST'])
    
    self.blueprint.add_url_rule('/cars/<int:id>', view_func=car_view, methods=['PUT', 'DELETE'])

  def get_blueprint(self):
    return self.blueprint