from db.connection import engine
from repositories.user_repository import UserRepository
from repositories.car_repository import CarRepository
from repositories.addresses_repositoy import AddressRepository

if __name__ == "__main__":

  #!Users
  user = UserRepository(engine)

  #*Add new user
#   user.add_user(
#     full_name = <name>, 
#     email = <email>",
#     phone_number = <number>
# )

  #*Get all users
  # user.get_all_users()

  #*Get user by id
  # user.get_user_by_id(<id>)

  #*Update user (data has to be passed as a dictionary)
  # user.update_user(
  #   _id = <user_id>,
  #   data = {
  #     <data as dict>
  #   }
  # )

  #*Delete user
  # user.delete_user(<id>)

  #!Cars
  car = CarRepository(engine)

  #*Add new car (user_id can be None)
  # car.add_car(
  #   make = <make>,
  #   model = <model>,
  #   year_of_manufacture = <year>
  # )

  #*Get all cars
  # car.get_all_cars()

  #*Get car by id
  # car.get_car_by_id(<id>)

  #*Update car (data has to be passed as a dictionary)
  # car.update_car(
  #   _id = <car_id>,
  #   data= {
  #     <data as dict>
  #   }
  # )

  #* Create a new car_user relation
  # car.create_car_user_relation(car_id = <car_id>, user_id = <user_id>)

  #*Delete car
  # car.delete_car(<car_id>)

  #!Addresses
  address = AddressRepository(engine)

  #*Add new address
  # # address.add_address(
  # #   street = "Calle 0, Avenida Central",
  # #   city = "San José",
  # #   province = "San José",
  # #   zip_code = "10101",
  # #   country = "Costa Rica",
  # #   user_id = 1
  # # )

  #*Get all addresses
  # address.get_all_address()

  #*Get address by id
  # address.get_address_by_id(<address_id>)

  #*Update address (data has to be passed as a dictionary)
  # address.update_address(
  #   _id = <address_id>,
  #   data= {
  #     <data as dict>
  #   }
  # )

  #*Delete address
  # address.delete_address(<id>)
