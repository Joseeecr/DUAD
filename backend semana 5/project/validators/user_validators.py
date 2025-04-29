class UserValidators:
  def __init__(self, user_repository):
    self.user_repository = user_repository

  def create_user_validator(self, data):
    errors = []

    if not data.get('email'):
      errors.append('Email is required')
    elif self.user_repository.is_email_taken(data["email"]):
      errors.append('Email already exists')

    if not data.get('full_name'):
      errors.append('Full name is required')

    if not data.get('user_name'):
      errors.append('Username is required')
    elif self.user_repository.is_username_taken(data["user_name"]):
      errors.append('Username already exists')

    if not data.get('password'):
      errors.append('Password is required')

    if not data.get('date_of_birth'):
      errors.append('Date of birth is required')

    if not data.get('status_account'):
      errors.append('Status account is required')

    return errors