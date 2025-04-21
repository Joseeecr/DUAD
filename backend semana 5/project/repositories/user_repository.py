class UserRepository:
  def __init__(self, db_manager):
    self.db_manager = db_manager


  def _format_user(self, user_record):
    return {
      'id': user_record[0],
      'full_name': user_record[1],
      'email': user_record[2],
      'user_name': user_record[3],
      'password': user_record[4],
      'date_of_birth' : user_record[5],
      'status_account': user_record[6]
    }


  def is_id_valid(self, _id):
    try:  
      result = self.db_manager.execute_query(
        "SELECT 1 FROM lyfter_car_rental.users WHERE id = %s LIMIT 1", (_id,)
      )
      return bool(result)
    except Exception as error:
      print('Some error occurred', error)
      return False


  def get_all_users(self):
    try:
      results = self.db_manager.execute_query(
        'SELECT id, full_name, email, user_name, password, date_of_birth, status_account '
        'FROM lyfter_car_rental.users ORDER BY id ASC'
      )
      formatted_results = [self._format_user(result) for result in results]
      return formatted_results


    except Exception as error:
      print('Error while getting all users', error)
      return False


  def get_filtered_users(self, filters):
    base_query = 'SELECT * FROM lyfter_car_rental.users'
    conditions = []
    values = []

    if 'id' in filters:
      conditions.append('id = %s')
      values.append(filters['id'])

    if 'full_name' in filters:
      conditions.append('full_name = %s')
      values.append(filters['full_name'])

    if 'status_account' in filters:
      conditions.append('status_account = %s')
      values.append(filters['status_account'])

    if 'email' in filters:
      conditions.append('email = %s')
      values.append(filters['email'])

    if 'user_name' in filters:
      conditions.append('user_name = %s')
      values.append(filters['user_name'])

    if 'date_of_birth' in filters:
      conditions.append('date_of_birth = %s')
      values.append(filters['date_of_birth'])

    if 'status_account' in filters:
      conditions.append('status_account = %s')
      values.append(filters['status_account'])

    if conditions:
      base_query += ' WHERE ' + ' AND '.join(conditions)

    return self.db_manager.execute_query_dict_result(base_query, tuple(values))


  def get_users_by_status_account(self, status_account):

    status = str(status_account).strip().casefold()
    valid_statuses = {stat.casefold() for stat in ['Currently renting', 'Currently not renting']}

    if status not in valid_statuses:
      raise ValueError('Invalid status. Only "Currently renting" or "Currently not renting" are allowed')

    try:
      results = self.db_manager.execute_query(
        'SELECT id, full_name, email, user_name, password, date_of_birth, status_account '
        'FROM lyfter_car_rental.users WHERE status_account ILIKE %s', (status_account,)
      )
      formatted_results = [self._format_user(result) for result in results]
      return formatted_results

    except Exception as error:
      print('Error while getting the specific user(s)', error)
      return False


  def is_email_taken(self, email):
    try:  
      result = self.db_manager.execute_query(
        "SELECT 1 FROM lyfter_car_rental.users WHERE email = %s LIMIT 1", (email,)
      )
      return bool(result)
    except Exception as error:
      print('Some error occurred', error)
      return False


  def is_username_taken(self, user_name):
    try:  
      result = self.db_manager.execute_query(
        "SELECT 1 FROM lyfter_car_rental.users WHERE user_name = %s LIMIT 1", (user_name,)
      )
      return bool(result)
    except Exception as error:
      print('Some error occurred', error)
      return False


  def insert_new_user_register(self, full_name, email, user_name, password, date_of_birth, status_account):
    status = str(status_account).strip().casefold()
    valid_statuses = {stat.casefold() for stat in ['Currently Renting', 'Currently not Renting']}

    if status not in valid_statuses:
      return {'error':'Invalid status. Only "Currently Renting" or "Currently not Renting" are allowed'}, 400

    try:
      self.db_manager.execute_query(
        'INSERT INTO lyfter_car_rental.users(full_name, email, user_name, password, date_of_birth, status_account) VALUES (%s, %s, %s, %s, %s, %s)',
        (full_name, email, user_name, password, date_of_birth, status_account.capitalize())
      )
      print('Inserted successfully')
      return {"message": "User created successfully"}, 201

    except Exception as error:
      print("Error inserting a user into the database: ", error)
      return {"message": "Failed to create user"}, 500


  def update_status_account(self, new_status_account, _id):
    if not self.is_id_valid(_id):
      return False
    
    status = str(new_status_account).strip().casefold()
    valid_statuses = {stat.casefold() for stat in ['Currently renting', 'Currently not renting']}
    
    if status not in valid_statuses:
      raise ValueError('Invalid status. Only "Currently renting" or "Currently not renting" are allowed')
    
    try:
      self.db_manager.execute_query(
        'UPDATE lyfter_car_rental.users SET status_account = %s WHERE ID = %s',
        (new_status_account, _id)
      )
      print('User status account updated successfully')
      return True
    
    except Exception as error:
      print('Error updating a user from the database:', error)
      return False


  def delete_user_register(self, _id):
    if self.is_id_valid(_id):
      try:
        self.db_manager.execute_query(
          'DELETE FROM lyfter_car_rental.users WHERE id = (%s)',(_id,)
        )
        print("User deleted successfully")
        return True
      except Exception as error:
        print('Error deleting a user from the database', error)
        return False
    else:
      return False


  def flag_delinquenter_user(self, _id):
    if self.is_id_valid(_id):
      try:
        self.db_manager.execute_query(
          'UPDATE lyfter_car_rental.users SET status_account = %s WHERE ID = %s',
          ('Delinquent', _id)
        )
        return True

      except Exception as error:
        print('Error occured', error)
        return False
    else:
      return False