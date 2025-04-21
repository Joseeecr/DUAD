from flask import jsonify, request
from flask.views import MethodView


class CarAPI(MethodView):
  def __init__(self, car_handler):
    self.car_handler = car_handler

  def get(self):

    filters = request.args.to_dict()

    if filters:
      cars = self.car_handler.get_cars_with_filters(filters)
    else:
      cars = self.car_handler.get_cars()

    return jsonify(cars), 200


  def post(self):
    data = request.get_json()
    response, status = self.car_handler.post_car(data)
    print(f'Response:{response} and status: {status}')
    return jsonify(response), status


  def put(self, id):
    data = request.get_json()
    if data:
      try:
        if self.car_handler.update_status_car(data, id):
          return {'Success': 'Car status has been updated'}, 200
        else:
          return {'Error': 'Car was not found or status was not allowed, "Available" or "Rented" are the only valid'}, 400
      except Exception as error:
        return {'Error': {error}}
    else:
      try:
        return self.car_handler.disabling_car(id)
      
      except Exception as error:
        print('Error occured while setting the car as "Disabled"', error)


  def delete(self, id):
    return self.car_handler.delete_car(id)