import json
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return json.load(file)


def write_json_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)