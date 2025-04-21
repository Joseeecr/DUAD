class CarRepository:
  def __init__(self, db_manager):
    self.db_manager = db_manager


  def _format_car(self, car_record):
    return {
      'id': car_record[0],
      'make': car_record[1],
      'model': car_record[2],
      'year_of_manufacture': car_record[3],
      'status_car ': car_record[4]
    }


  def is_id_valid(self, _id):
    try:  
      result = self.db_manager.execute_query(
        "SELECT 1 FROM lyfter_car_rental.cars WHERE id = %s LIMIT 1", (_id,)
      )
      return bool(result)
    except Exception as error:
      print('Some error occurred', error)
      return False


  def get_all_cars(self):
    try:
      results = self.db_manager.execute_query(
        'SELECT id, make, model, year_of_manufacture, status_car '
        'FROM lyfter_car_rental.cars ORDER BY id ASC'
      )
      formatted_results = [self._format_car(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting all cars', error)
      return False


  def get_filtered_cars(self, filters):
    base_query = 'SELECT * FROM lyfter_car_rental.cars'
    conditions = []
    values = []

    if 'id' in filters:
      conditions.append('id = %s')
      values.append(filters['id'])

    if 'make' in filters:
      conditions.append('make = %s')
      values.append(filters['make'])

    if 'model' in filters:
      conditions.append('model = %s')
      values.append(filters['model'])

    if 'year_of_manufacture' in filters:
      conditions.append('year_of_manufacture = %s')
      values.append(filters['year_of_manufacture'])

    if 'status_car' in filters:
      conditions.append('status_car = %s')
      values.append(filters['status_car'])

    if conditions:
      base_query += ' WHERE ' + ' AND '.join(conditions)

    return self.db_manager.execute_query_dict_result(base_query, tuple(values))


  def get_cars_by_status_car(self, status_car):

    status = str(status_car).strip().casefold()
    valid_statuses = {stat.casefold() for stat in ['Available', 'Rented']}

    if status not in valid_statuses:
      raise ValueError('Invalid status. Only "Available" or "Rented" are allowed')

    try:
      results = self.db_manager.execute_query(
        'SELECT id, make, model, year_of_manufacture, status_car '
        'FROM lyfter_car_rental.cars WHERE status_car ILIKE %s', (status_car,)
      )
      formatted_results = [self._format_car(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting the specific car(s)', error)
      return False


  def insert_new_car_register(self, make, model, year_of_manufacture, status_car):
    try:
      self.db_manager.execute_query(
        'INSERT INTO lyfter_car_rental.cars(make, model, year_of_manufacture, status_car) VALUES (%s, %s, %s, %s)',
        (make, model, year_of_manufacture, status_car),
      )
      print('Inserted successfully')
      return True

    except Exception as error:
      print("Error inserting a car into the database: ", error)
      return False


  def update_status_car(self, new_status_car, _id):
    if not self.is_id_valid(_id):
      return False

    status_car = str(new_status_car).casefold().strip()
    valid_statuses = {stat.casefold() for stat in ['Rented', 'Available']}

    if status_car not in valid_statuses:
      raise ValueError('Invalid status. Only "Rented" and "Available" are allowed.')

    try:
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.cars SET status_car = %s WHERE ID = %s',
        (status_car.capitalize(), _id)
      )
      print('Car status updated successfully')
      return True
    
    except Exception as error:
      print('Error updating a car from the database:', error)
      return False


  def disable_car(self, _id):
    if self.is_id_valid(_id):
      try:
        self.db_manager.execute_query(
          'UPDATE lyfter_car_rental.cars SET status_car = %s WHERE ID = %s',
          ('Disabled', _id)
        )
        print('Car successfuly disabled')
        return True

      except Exception as error:
        print('Error occured in the DB while disabling a car', error)
        return False
    else:
      return False


  def delete_car_register(self, _id):
    if self.is_id_valid(_id):
      try:
        self.db_manager.execute_query(
          'DELETE FROM lyfter_car_rental.cars WHERE id = (%s)',(_id,)
        )
        print("Car was deleted successfully")
        return True

      except Exception as error:
        print('Error deleting a car from the database', error)
        return False
    else:
      return False