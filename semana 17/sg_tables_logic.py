import PySimpleGUI as sg 
from validators import Validators

class CategoryDataManager:

    def __init__(self, category_data_list=None):
        self.category_data_list = category_data_list if category_data_list is not None else []

    def process_user_category(self, category_window, values):
        user_category_input = values["-CATEGORY-"]

        if Validators.validate_user_input(user_category_input):
            if Validators.is_duplicate_category(user_category_input, self.category_data_list): # Two ifs were created to show more specific errors
                self.category_data_list.append(user_category_input)
        else:
            sg.popup("Enter a valid category!")
        
        category_window["-CATEGORY_TABLE-"].update(values=self.category_data_list)
        category_window["-CATEGORY-"].update("")


class UserDataManager:

    def __init__(self, user_data_list=None):
        self.user_data_list = user_data_list if user_data_list is not None else []

    def add_user_data_to_list(self, main_window, values, transaction_type):
        user_title_input = (values["-TITLE-"])
        user_amount_input = values["-AMOUNT-"]
        selected_category = values["-CATEGORY-"]

        if not Validators.validate_user_input(user_title_input):
            sg.popup("Invalid title")
            return
            
        if not user_amount_input.isdigit():
            sg.popup("Amount must be a number")
            return
        
        if not selected_category:
            sg.popup("Please select a category")
            return

        new_entry = {
                "title": user_title_input,
                "category": selected_category,
                "type": transaction_type,
                "amount": int(user_amount_input)
            }
        self.user_data_list.append(new_entry)
        self.update_table(main_window)

    def update_table(self, main_window):
        main_window["-MAIN_TABLE-"].update(values=[list(data.values()) for data in self.user_data_list])