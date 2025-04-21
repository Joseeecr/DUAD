from flask import Blueprint
from api.views.car_user_view import CarUserAPI

class CarUserBlueprint:
  def __init__(self, car_user_handler):
    self.car_user_handler = car_user_handler
    self.blueprint = Blueprint('cars_users', __name__)
    self._register_routes()


  def _register_routes(self):
    car_user_view = CarUserAPI.as_view('car_user_api', car_user_handler=self.car_user_handler)

    self.blueprint.add_url_rule('/rentals', view_func=car_user_view, methods=['GET', 'POST'])
    
    self.blueprint.add_url_rule('/rentals/<int:id>', view_func=car_user_view, methods=['PUT', 'DELETE'])

  def get_blueprint(self):
    return self.blueprint