import ast

class CarUserValidators:
  def __init__(self, car_user_repository):
    self.car_user_repository = car_user_repository

  def create_register_validator(self, data):
    errors = []

    if not data.get('user_id'):
      errors.append('User id is required')
    
    if not self.car_user_repository.is_id_valid(data.get('user_id')):
      errors.append('User id does not exist')

    if not data.get('car_id'):
      errors.append('Car id is required')
    
    if not self.car_user_repository.is_id_valid(data.get('car_id')):
      errors.append('Car id does not exist')

    return errors
  
  def update_register_validator(self, new_rental_status, _id):
    errors = []

    if not self.car_user_repository.is_id_valid(_id):
      errors.append('Rental id does not exist')

    rental_status = str(new_rental_status).casefold().strip()
    valid_statuses = {stat.casefold() for stat in ['Active', 'Completed']}
    rental_status = ast.literal_eval(rental_status)

    if rental_status.get('rental_status') not in valid_statuses:
      errors.append('Invalid status, Only "Active" and "Completed" are allowed')

    return errors