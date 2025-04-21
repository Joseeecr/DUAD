class CarValidators:
  def __init__(self, car_repository):
    self.car_repository = car_repository

  def create_car_validator(self, data):
    errors = []

    if not data.get('make'):
      errors.append('Make is required')

    if not data.get('model'):
      errors.append('Model is required')

    if not data.get('year_of_manufacture'):
      errors.append('Year of manufacture is required')

    if not data.get('status_car'):
      errors.append('Status car is required')

    return errors