from flask import jsonify

class UserHandler:

  def __init__(self, user_repository, user_validator):
    self.user_repository = user_repository
    self.user_validator = user_validator

  def get_users(self):
    return self.user_repository.get_all_users()


  def get_users_with_filters(self, filters):
    return self.user_repository.get_filtered_users(filters)


  def post_user(self, data):
    errors = self.user_validator.create_user_validator(data)
    if errors:
      return {'errors': errors}, 400

    try:
      full_name = data.get('full_name')
      email = data.get('email')
      user_name = data.get('user_name')
      password = data.get('password')
      date_of_birth = data.get('date_of_birth')
      status_account = data.get('status_account')

      response, status = self.user_repository.insert_new_user_register(
        full_name, email, user_name, password, date_of_birth, status_account
      )

      return response, status

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


  def update_user_status_account(self, data, _id):
  
    try:
      response, status= self.user_repository.update_status_account(data.get('status_account'), _id)
      return response, status

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


    except Exception as error:
      print('Error happened while updating the user status', error)


  def delete_user(self, _id):
    if self.user_repository.delete_user_register(_id):
      return {'Success': 'User deleted successfully'}
    else:
      return {'Error':'User id was not found'}, 404


  def flag_delinquenter_user(self, _id):
    return self.user_repository.flag_delinquenter_user(_id)
