from flask import jsonify, request
from flask.views import MethodView


class UserAPI(MethodView):
  def __init__(self, user_handler):
    self.user_handler = user_handler

  def get(self):

    filters = request.args.to_dict()

    if filters:
      users = self.user_handler.get_users_with_filters(filters)
    else:
      users = self.user_handler.get_users()

    return jsonify(users), 200


  def post(self):
    data = request.get_json()
    response, status = self.user_handler.post_user(data)
    return jsonify(response), status


  def put(self, id):
    data = request.get_json()

    return self.user_handler.update_user_status_account(data, id)


  def patch(self, id):
    return self.user_handler.flag_delinquenter_user(id)


  def delete(self, id):
    return self.user_handler.delete_user(id)