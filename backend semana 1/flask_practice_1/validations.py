def is_empty(value):
    return not value or not value.strip()


def validate_type(value):

    if isinstance(value, str):
        if value.isdigit():
            return f"Not Valid: You should include text, not only digits", 400

    elif isinstance(value, int):
        return f"Not Valid: You should include text, not only digits", 400
    
    return None


def validate_id(id_value, tasks_list):
    if not isinstance(id_value["id"], int):
        return "Not Valid: ID must be a number", 400

    if any(task["id"] == id_value["id"] for task in tasks_list):
        return "Not Valid: ID already exists", 400

    return None


def validate_title(title_value):

    incorrect_type = validate_type(title_value)

    if incorrect_type:
        return incorrect_type

    if is_empty(title_value):
        return "Not Valid: empty values are not allowed", 400

    return None


def validate_description(description_value):
    incorrect_type = validate_type(description_value)

    if incorrect_type:
        return incorrect_type

    if is_empty(description_value):
        return "Not Valid: empty values are not allowed", 400
    
    return None


def validate_status(status_value):
    if status_value.lower() not in ["To Do".lower(), "In Progress".lower(), "Completed".lower()]:
        return "Not valid: Status must be 'To do', 'In Progress' or 'Completed'", 400

    return None