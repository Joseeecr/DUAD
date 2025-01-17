from read_and_add_data_to_files import read_json_file, add_data_to_json_file
from validations import validate_id, validate_title, validate_description, validate_status 
from flask import request


def add_task_logic():
    tasks_list = read_json_file("tasks_file.json")
    
    try:
        new_task = {
                    "id": request.json["id"],
                    "title": request.json["title"],
                    "description": request.json["description"],
                    "status": request.json["status"]
        }
    except KeyError as ex:
        return f"Missing field: {ex.args[0]}", 400

    errors = [
        validate_id(new_task, tasks_list),
        validate_title(new_task["title"]),
        validate_description(new_task["description"]),
        validate_status(new_task["status"]),
    ]
    
    errors= [error for error in errors if error]
    if errors:
        return {"errors": errors}, 400

    tasks_list.append(new_task)

    add_data_to_json_file("tasks_file.json", tasks_list)

    return tasks_list


def get_tasks_logic():
    tasks_list = read_json_file("tasks_file.json")
    filtered_tasks = tasks_list
    state_filter = request.args.get("status")
    
    if state_filter:
        if state_filter.lower() not in ["To Do".lower(), "In Progress".lower(), "Completed".lower()]:
            return "Not valid: Status must be 'To do', 'In Progress' or 'Completed'", 400
        else:
            state_filter = state_filter.lower()
            filtered_tasks = list(
                filter(lambda task: task["status"].lower() == state_filter, filtered_tasks)
            )

    return {"data": filtered_tasks}


def delete_tasks_logic(id_):
    tasks_list = read_json_file("tasks_file.json")

    for task in tasks_list:
        if task["id"] == id_:
            tasks_list.remove(task)
        
            add_data_to_json_file("tasks_file.json", tasks_list)

            return "Task succesfully deleted"

    return "Task not found", 404


def edit_task_logic(id_, update_data):
    tasks_list = read_json_file("tasks_file.json")
    task_to_modify = None

    for task in tasks_list:
        if task["id"] == id_:
            task_to_modify = task
            break

    if task_to_modify is None:
        return "Task not found", 404

    errors = []
    for key in update_data.keys():
        if key in task_to_modify:
            if key == "id":
                error = validate_id(update_data, tasks_list)
            elif key == "title":
                error = validate_title(update_data["title"])
            elif key == "description":
                error = validate_description(update_data["description"])
            elif key == "status":
                error = validate_status(update_data["status"])

            if error:
                errors.append({key : error})

    if errors:
        return {"errors": errors}, 400

    for key, value in update_data.items():
        if key in task_to_modify:
            task_to_modify[key] = value

    add_data_to_json_file("tasks_file.json", tasks_list)

    return "Task succesfully edited"