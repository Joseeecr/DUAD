import re
import PySimpleGUI as sg


class Validators:

    @classmethod
    def validate_user_input(self, user_input):
        pattern = r'^[a-zA-Z]+\s*\S$'
        return re.match(pattern, user_input) is not None
    
    @classmethod
    def is_duplicate_category(self, user_input, category_data_list):

        if user_input in category_data_list:
            sg.popup("Duplicate categories are not allowed!")
            return False
        return True