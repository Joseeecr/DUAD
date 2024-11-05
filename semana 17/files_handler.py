import PySimpleGUI as sg
import os
import json


class CategoryFileHandler:

    def __init__(self, category_data_manager):
        self.category_data_manager = category_data_manager

    def save_to_json(self, file_path):

        with open(file_path, "w") as file:
            json.dump(self.category_data_manager.category_data_list, file)

    def load_from_json(self, file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file:
                return json.load(file)
        return None

class IncomeOutFileHandler:

    def __init__(self, user_data_manager):
        self.user_data_manager = user_data_manager


    def save_to_json(self, file_path):
        with open(file_path, "w") as file:
            json.dump(self.user_data_manager.user_data_list, file, indent=4)

    def load_from_json(self, file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file:
                return json.load(file)
        return None
