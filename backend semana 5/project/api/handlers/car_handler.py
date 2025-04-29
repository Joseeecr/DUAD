from flask import jsonify

class CarHandler:

  def __init__(self, car_repository, car_validator):
    self.car_repository = car_repository
    self.car_validator = car_validator


  def get_cars(self):
    return self.car_repository.get_all_cars()


  def get_cars_with_filters(self, filters):
    return self.car_repository.get_filtered_cars(filters)


  def post_car(self, data):
    errors = self.car_validator.create_car_validator(data)
    if errors:
      return {'errors': errors}, 400

    try:
      make = data.get('make')
      model = data.get('model')
      year_of_manufacture = data.get('year_of_manufacture')
      status_car = data.get('status_car')

      response, status = self.car_repository.insert_new_car_register(
        make, model, year_of_manufacture, status_car
      )

      return response, status

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


  def update_status_car(self, data, _id):
    try:
      response, status= self.car_repository.update_status_car(data.get('status_car'), _id)
      return response, status

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


  def disabling_car(self, _id):
    return self.car_repository.disable_car(_id)


  def delete_car(self, _id):
    if self.car_repository.delete_car_register(_id):
      return {'Success': 'Car deleted successfully'}
    else:
      return {'Error':'Car id was not found'}, 404