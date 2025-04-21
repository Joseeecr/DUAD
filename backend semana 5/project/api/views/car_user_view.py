from flask import jsonify, request
from flask.views import MethodView


class CarUserAPI(MethodView):
  def __init__(self, car_user_handler):
    self.car_user_handler = car_user_handler

  def get(self):

    filters = request.args.to_dict()

    if filters:
      registers = self.car_user_handler.get_registers_with_filters(filters)
    else:
      registers = self.car_user_handler.get_registers()

    if isinstance(registers, tuple):
      return jsonify(registers[0]), (registers[1])


    return jsonify(registers), 200


  def post(self):
    data = request.get_json()
    print(f'Received data: {data}')
    response, status = self.car_user_handler.post_register(data)
    print(f'Response: {response}, status: {status}')
    return jsonify(response), status


  def put(self, id):
    data = request.get_json()

    if data:
      response, status = self.car_user_handler.update_status(data, id)
      return jsonify(response), status
    else:
      response, status = self.car_user_handler.complete_rental_handler(id)
      return jsonify(response), status


  def delete(self, id):
    return self.car_user_handler.delete_rental(id)