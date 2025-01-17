from flask import Flask, request
from requests_handling import add_task_logic, get_tasks_logic, delete_tasks_logic, edit_task_logic
from flask.views import MethodView

app = Flask(__name__)


class HandlerAPI(MethodView):


    def get(self):
        get_task = get_tasks_logic()
        return get_task


    def post(self):
        new_task = add_task_logic()
        return new_task


    def delete(self, id_):
        deleted_task = delete_tasks_logic(id_)

        return deleted_task


    def patch(self, id_):
        update_data = request.json

        result = edit_task_logic(id_, update_data)

        return result

api_view = HandlerAPI.as_view("handler_api")

app.add_url_rule("/get_tasks/", view_func=api_view, methods=["GET"])
app.add_url_rule("/add_task/", view_func=api_view, methods=["POST"])
app.add_url_rule("/delete_task/<int:id_>/", view_func=api_view, methods=["DELETE"])
app.add_url_rule("/edit_task/<int:id_>/", view_func=api_view, methods=["PATCH"])


if __name__ == "__main__":
    app.run(host="localhost", debug=True)