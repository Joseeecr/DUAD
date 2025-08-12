from sqlalchemy import select
from db.models import user_table
from exceptions.exceptions import NotFoundError
import bcrypt 


class UserService:
  def __init__(self, user_validator, user_repository, jwt_manager):
    self.user_validator = user_validator
    self.user_repository = user_repository
    self.jwt_manager = jwt_manager


  def list_users(self, params : dict) -> list[dict]:
    filters  = self.user_validator.validate_filters(params)

    stmt = (select(
      user_table.c.id,
      user_table.c.name,
      user_table.c.last_name,
      user_table.c.email,
      user_table.c.phone_number,
      user_table.c.is_admin
    ))

    if "id" in filters:
      stmt = stmt.where(user_table.c.id == filters["id"])

    if "name" in filters:
      stmt = stmt.where(user_table.c.name == filters["name"])

    if "last_name" in filters:
      stmt = stmt.where(user_table.c.last_name == filters["last_name"])

    if "email" in filters:
      stmt = stmt.where(user_table.c.email == filters["email"])

    if "is_admin" in filters:
      stmt = stmt.where(user_table.c.is_admin == filters["is_admin"])

    result = self.user_repository.get_users(stmt)
  
    users = [dict(row._mapping) for row in result]

    if not users:
      raise NotFoundError("No matching users found.")

    
    return users


  def insert_user(self, data : dict) -> str:
    validate_data = self.user_validator.validate_insert_user(data)

    password = validate_data.get("password").encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pwd  = bcrypt.hashpw(password, salt).decode("utf-8")

    validate_data["password"] = hashed_pwd

    user_id = self.user_repository.insert_user(validate_data)

    token = self.jwt_manager.encode(
      {
        "id": user_id,      
        "is_admin": validate_data["is_admin"]
      }
    )

    return token


  def login_user(self, email : str, password : str) -> str:
    user = self.user_repository.get_user_by_email(email)

    if user is None:
      raise ValueError("Incorrect email or password")
    
    stored_hash = user["password"].encode("utf-8") if isinstance(user["password"], str) else user["password"]
    
    if not bcrypt.checkpw(password.encode("utf-8"), stored_hash):
      raise ValueError("Incorrect email or password")
    
    token = self.jwt_manager.encode({
      "id": user["id"],
      "is_admin": user["is_admin"]
    })

    return token


  def update_user_by_admin(self, user_id : int, data : dict):
    user = self.user_repository.get_user_by_id(user_id)

    if not user:
      raise ValueError("User not found")
    
    validate_data = self.user_validator.validate_update_user(data)

    return self.user_repository.update_user_by_admin(user_id, validate_data)


  def delete_user(self, user_id : int):
    user = self.user_repository.get_user_by_id(user_id)

    if not user:
      raise ValueError("User not found")
  
    return self.user_repository.delete_user(user_id)