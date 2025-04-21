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
    if data:
      try:
        if self.user_handler.update_user_status_account(data, id):
          return {'Success': 'User status has been updated'}, 200
        else:
          return {'Error': 'User was not found or status was not allowed, "Currently renting" or "Currently not renting" are the only valid'}, 400
      except Exception as error:
        return {'Error': {error}}
    else:
      try:
        return self.user_handler.flag_delinquenter_user(id)
      
      except Exception as error:
        print('Error occured while setting the user as "Delinquent"', error)


  def delete(self, id):
    return self.user_handler.delete_user(id)