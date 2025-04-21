from flask import Blueprint
from api.views.user_view import UserAPI

class UserBlueprint:
  def __init__(self, user_handler):
    self.user_handler = user_handler
    self.blueprint = Blueprint('users', __name__)
    self._register_routes()


  def _register_routes(self):
    user_view = UserAPI.as_view('user_api', user_handler=self.user_handler)

    self.blueprint.add_url_rule('/users', view_func=user_view, methods=['GET', 'POST'])
    
    self.blueprint.add_url_rule('/users/<int:id>', view_func=user_view, methods=['PUT', 'DELETE'])

  def get_blueprint(self):
    return self.blueprint