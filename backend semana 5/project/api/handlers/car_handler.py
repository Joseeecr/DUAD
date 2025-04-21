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

      success = self.car_repository.insert_new_car_register(
        make, model, year_of_manufacture, status_car
      )


      if success:
        return {"message": "Car created successfully"}, 201
      else:
        return {"message": "Failed to create car"}, 500

    except Exception as error:
      return jsonify({"message": "Error", "details": str(error)}), 400


  def update_status_car(self, data, _id):
    try:
      new_status = data.get('status_car')
      new_status = new_status.lower().capitalize()

      if new_status is not None:
        return self.car_repository.update_status_car(new_status, _id)
      else:
        return False

    except Exception as error:
      print('Error happened while updating the car status', error)


  def disabling_car(self, _id):
    try:
      if self.car_repository.disable_car(_id):
        return  {'Success': 'Car disabled successfully'}, 200
      else:
        return {'Error': 'Error while labeling the car as disabled'}, 400
    except Exception as error:
      print('Error happened while labeling the car', error)


  def delete_car(self, _id):
    if self.car_repository.delete_car_register(_id):
      return {'Success': 'Car deleted successfully'}
    else:
      return {'Error':'Car id was not found'}, 404