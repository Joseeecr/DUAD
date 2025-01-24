from flask import Flask, request
from requests_handling import add_task_logic, get_tasks_logic, delete_tasks_logic, edit_task_logic

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Welcome to the home page</h1>"


@app.route("/get_tasks")
def get_tasks():
    get_task = get_tasks_logic()
    return get_task


@app.route("/add_task", methods=["POST"])
def add_task():
    new_task = add_task_logic()
    return new_task


@app.route("/delete_task/<int:id_>", methods=["DELETE"])
def delete_task(id_):
    deleted_task = delete_tasks_logic(id_)

    return deleted_task


@app.route("/edit_task/<int:id_>", methods=["PATCH"])
def edit_task(id_):
    update_data = request.json

    result = edit_task_logic(id_, update_data)

    return result


if __name__ == "__main__":
    app.run(host="localhost", debug=True)