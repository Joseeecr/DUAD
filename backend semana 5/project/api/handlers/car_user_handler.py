from flask import jsonify

class CarUserHandler:

  def __init__(self, car_user_repository, car_user_validator):
    self.car_user_repository = car_user_repository
    self.car_user_validator = car_user_validator


  def get_registers(self):
    return self.car_user_repository.get_all_registers()


  def get_registers_with_filters(self, filters):
    return self.car_user_repository.get_filtered_registers(filters)


  def post_register(self, data):
    errors = self.car_user_validator.create_register_validator(data)
    if errors:
      return {'errors': errors}, 400

    user_id = data.get('user_id')
    car_id = data.get('car_id')
      

    response, status = self.car_user_repository.create_new_rental(user_id, car_id)
    return response, status


  def update_status(self, data, _id):
    errors = self.car_user_validator.update_register_validator(data, _id)
    if errors:
      return {'errors': errors}, 400

    try:
      rental_status = data.get('rental_status')

      success = self.car_user_repository.update_rental_status(rental_status, _id)

      if success:
        return {"message": "Rental status updated successfully"}, 201
      else:
        return {"message": "Failed to update rental"}, 500

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


  def complete_rental_handler(self, rental_id):
    return self.car_user_repository.complete_rental(rental_id)


  def delete_rental(self, _id):
    if self.car_user_repository.delete_register(_id):
      return {'Success': 'Rental deleted successfully'}
    else:
      return {'Error':'Rental id was not found'}, 404