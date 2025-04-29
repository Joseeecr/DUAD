from repositories.user_repository import UserRepository
from repositories.car_repository import CarRepository
from repositories.car_user_repository import CarUserRepository
from config.database import PgManager
from api.handlers.user_handler import UserHandler
from api.routes.user_routes import UserBlueprint
from validators.user_validators import UserValidators
from api.handlers.car_handler import CarHandler
from api.routes.car_routes import CarBlueprint
from validators.car_validators import CarValidators
from api.handlers.car_user_handler import CarUserHandler
from api.routes.car_user_routes import CarUserBlueprint
from validators.car_user_validators import CarUserValidators
from flask import Flask

db_manager = PgManager(
  dbname="postgres",
  user="postgres",
  password="54321",
  host="localhost"
)

app = Flask(__name__)


#* users repo
users_repo = UserRepository(db_manager)
user_validator = UserValidators(users_repo)
user_handler = UserHandler(users_repo, user_validator)
user_bp_instance = UserBlueprint(user_handler)

#* cars repo
cars_repo = CarRepository(db_manager)
car_validator = CarValidators(cars_repo)
car_handler = CarHandler(cars_repo, car_validator)
car_bp_instance = CarBlueprint(car_handler)


#* car_user repo
car_user_repo = CarUserRepository(db_manager)
car_user_validator = CarUserValidators(car_user_repo)
car_user_handler = CarUserHandler(car_user_repo, car_user_validator)
car_user_bp_instance = CarUserBlueprint(car_user_handler)

app.register_blueprint(user_bp_instance.get_blueprint(), url_prefix="/api")
app.register_blueprint(car_bp_instance.get_blueprint(), url_prefix="/api")
app.register_blueprint(car_user_bp_instance.get_blueprint(), url_prefix="/api")

if __name__ == "__main__":
    app.run(host="localhost", debug=True)