class CarUserRepository:
  def __init__(self, db_manager):
    self.db_manager = db_manager


  def _format_register(self, register_record):
    return {
      'id': register_record[0],
      'user_id': register_record[1],
      'car_id': register_record[2],
      'rental_date': register_record[3],
      'rental_status ': register_record[4]
    }


  def is_id_valid(self, _id):
    try:  
      result = self.db_manager.execute_query(
        "SELECT 1 FROM lyfter_car_rental.users_cars WHERE id = %s LIMIT 1", (_id,)
      )
      return bool(result)
    except Exception as error:
      print('Some error occurred', error)
      return False


  def get_all_registers(self):
    try:
      results = self.db_manager.execute_query(
        'SELECT id, user_id, car_id, rental_date, rental_status '
        'FROM lyfter_car_rental.users_cars ORDER BY id ASC'
      )
      formatted_results = [self._format_register(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting all registers', error)
      return False


  def get_filtered_registers(self, filters):
    base_query = 'SELECT * FROM lyfter_car_rental.users_cars'
    conditions = []
    values = []

    if 'id' in filters:
      if not self.is_id_valid(filters['id']):
        return {'error': 'id does not exist'}, 404
      conditions.append('id = %s')
      values.append(filters['id'])


    if 'user_id' in filters:
      if not self.is_id_valid(filters['user_id']):
        return {'error': 'User id does not exist'}, 404
      conditions.append('user_id = %s')
      values.append(filters['user_id'])

    if 'car_id' in filters:
      if not self.is_id_valid(filters['car_id']):
        return {'error': 'Car id does not exist'}, 404
      conditions.append('car_id = %s')
      values.append(filters['car_id'])

    if 'rental_date' in filters:
      conditions.append('rental_date = %s')
      values.append(filters['rental_date'])

    if 'rental_status' in filters:
      conditions.append('rental_status = %s')
      values.append(filters['rental_status'])

    if conditions:
      base_query += ' WHERE ' + ' AND '.join(conditions)

    return self.db_manager.execute_query_dict_result(base_query, tuple(values))


  def get_register_by_id(self, _id):
    try:
      results = self.db_manager.execute_query(
        'SELECT id, user_id, car_id, rental_date, rental_status '
        'FROM lyfter_car_rental.users_cars WHERE id = (%s)', (_id,)
      )
      formatted_results = [self._format_register(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting the specific register', error)
      return False


  def get_registers_by_rental_status(self, rental_status):

    status = str(rental_status).strip().casefold()
    valid_statuses = {stat.casefold() for stat in ['Active', 'Completed']}

    if status not in valid_statuses:
      raise ValueError('Invalid status. Only "Available" or "Rented" are allowed')

    try:
      results = self.db_manager.execute_query(
        'SELECT id, user_id, car_id, rental_date, rental_status '
        'FROM lyfter_car_rental.users_cars WHERE rental_status ILIKE %s', (rental_status,)
      )
      formatted_results = [self._format_register(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting the specific register', error)
      return False


  def create_new_rental(self, user_id, car_id):
    check_status_car = self.db_manager.execute_query(
      'SELECT 1 FROM lyfter_car_rental.cars WHERE id = %s AND status_car = %s', (car_id, 'Available')
    )

    if not check_status_car:
      return {'error': 'only cars that are "Available" can be rented'}, 400

    try:
      self.db_manager.execute_query(
      'INSERT INTO lyfter_car_rental.users_cars (user_id, car_id, rental_status, rental_date) '
      'VALUES (%s, %s, %s, CURRENT_DATE)', (user_id, car_id, 'Active')
      )
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.cars SET status_car = %s WHERE id = %s',
        ('Rented', car_id)
      )
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.users SET status_account = %s WHERE id = %s',
        ('Currently renting', user_id)
      )
      print('New rental was succesfully created!')
      return {'message': 'Rental created successfully'}, 201

    except Exception as error:
      print("Error ocurred when creating a new rental in the DB", error)
      return {'error': f'Unexpected error: {str(error)}'}, 500


  def update_rental_status(self, new_rental_status, _id):
  
    try:
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.users_cars SET rental_status = %s WHERE ID = %s',
        (new_rental_status, _id)
      )
      print('Rental status updated successfully')
      return True
    
    except Exception as error:
      print('Error updating a car from the database:', error)
      return False


  def complete_rental(self, rental_id):

    rental_info = self.db_manager.execute_query(
        '''
        SELECT car_id, user_id, rental_status
        FROM lyfter_car_rental.users_cars
        WHERE id = %s
        ''',
        (rental_id,)
    )

    if not rental_info:
      return {'Error':'Rental not found'}, 404

    car_id, user_id, rental_status = rental_info[0]

    if rental_status != 'Active':
      return {'Error':'Invalid status, in order to complete the rental, the rental status must be "Active"'}, 400

    try:
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.users_cars SET rental_status = %s  WHERE id = %s',
        ('Completed', rental_id)
      )

      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.cars SET status_car = %s WHERE id = %s',
        ('Available', car_id)
      )

      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.users SET status_account = %s WHERE id = %s',
        ('Currently not renting', user_id)
      )

      print('Rental was successfully completed')
      return {'success': 'Rental was successfully completed'}, 200

    except Exception as error:
      print('Error occured while completing the rental', error)
      return {'error': f'Unexpected error: {str(error)}'}, 500


  def delete_register(self, _id):
    if not self.is_id_valid(_id):
      return False

    try:
      self.db_manager.execute_query(
        'DELETE FROM lyfter_car_rental.users_cars WHERE id = (%s)',(_id,)
      )
      print("Register was deleted successfully")
      return True

    except Exception as error:
      print('Error deleting a register from the database', error)
      return False