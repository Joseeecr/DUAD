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

    return jsonify(response), status


  def put(self, id):
    data = request.get_json()

    return self.car_handler.update_status_car(data, id)


  def patch(self, id):
    return self.car_handler.disabling_car(id)


  def delete(self, id):
    return self.car_handler.delete_car(id)