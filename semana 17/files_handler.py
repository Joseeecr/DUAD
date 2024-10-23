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

    def update_table_with_json_file(self, category_window):
        json_data = self.load_from_json("semana 17/categories_file.json")
        json_data = [[item] for item in self.category_data_manager.category_data_list]
        if json_data:
            category_window["-CATEGORY_TABLE-"].update(values=json_data)

    def delete_item(self, category_window):
        self.category_data_manager.user_input = sg.popup_get_text("Enter a value", 'Deleting item')

        if self.category_data_manager.user_input in self.category_data_manager.category_data_list:
            self.category_data_manager.category_data_list.remove(self.category_data_manager.user_input)
            self.save_to_json("semana 17/categories_file.json")

            category_window["-CATEGORY_TABLE-"].update(values=self.category_data_manager.category_data_list)

        elif self.category_data_manager.user_input is not None and self.category_data_manager.user_input not in self.category_data_manager.category_data_list:
            sg.popup("That item doesn't exist")


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

    def update_table_with_json_file(self, main_window):
        json_data = self.load_from_json("semana 17/user_data_file.json")
        json_data = [[item["title"], item["category"], item["type"], item["amount"]] for item in self.user_data_manager.user_data_list]
        if json_data:
            main_window["-MAIN_TABLE-"].update(values=json_data)

    def delete_item(self, values, main_window):
        selected_row = values["-MAIN_TABLE-"]

        if not selected_row:
            sg.popup("Please select a row to delete")

        else:
            index_to_delete = selected_row[0]
            if 0 <= index_to_delete < len(self.user_data_manager.user_data_list):
                removed_item  = self.user_data_manager.user_data_list.pop(index_to_delete)
                sg.popup(f"Row with Title: {removed_item["title"]} and Category: {removed_item["category"]} was deleted")
                self.save_to_json("semana 17/user_data_file.json")
                main_window["-MAIN_TABLE-"].update(values=self.user_data_manager.update_table(main_window))

