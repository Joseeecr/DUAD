import PySimpleGUI as sg


class CategoryUI:
    
    def __init__(self, category_data_manager, category_file_handler):
        self.category_data_manager = category_data_manager
        self.category_file_handler = category_file_handler
        self.category_header = ["Category"]

        if category_data_manager.category_data_list is None:
            category_data_manager.category_data_list = []

        self.window_category_layout = [
            [sg.Table(
                values=[[cat] for cat in self.category_data_manager.category_data_list] ,
                headings= self.category_header,
                key= "-CATEGORY_TABLE-"
            )],
            [sg.Text("Add the Category name"), sg.InputText(key="-CATEGORY-")],
            [sg.Button("Save Category"), sg.Button("Close"), sg.Button("Delete")],
        ]

    def update_table_with_json_file(self, category_window):
        json_data = self.category_file_handler.load_from_json("categories_file.json")
        json_data = [[item] for item in self.category_data_manager.category_data_list]
        if json_data:
            category_window["-CATEGORY_TABLE-"].update(values=json_data)
        
    def delete_item(self, category_window):
        self.category_data_manager.user_input = sg.popup_get_text("Enter a value", 'Deleting item')

        if self.category_data_manager.user_input in self.category_data_manager.category_data_list:
            self.category_data_manager.category_data_list.remove(self.category_data_manager.user_input)
            self.category_file_handler.save_to_json("categories_file.json")

            category_window["-CATEGORY_TABLE-"].update(values=self.category_data_manager.category_data_list)

        elif self.category_data_manager.user_input is not None and self.category_data_manager.user_input not in self.category_data_manager.category_data_list:
            sg.popup("That item doesn't exist")

    def open_category_window(self):

        category_window = sg.Window("Add New Category", self.window_category_layout)
        event, values = category_window.read(timeout=5)
        self.update_table_with_json_file(category_window)
        
        while True:
            event, values = category_window.read()

            if event == sg.WINDOW_CLOSED or event == "Close":
                break
            elif event == "Save Category":
                self.category_data_manager.process_user_category(category_window, values)
                self.category_file_handler.save_to_json("categories_file.json")
            elif event == "Delete":
                self.delete_item(category_window)

        category_window.close()


class IncomeOutUI:
    
    def __init__(self, user_data_manager, category_data_manager, income_out_file_handler, main_window):
        self.user_data_manager = user_data_manager
        self.category_data_manager = category_data_manager
        self.income_out_file_handler = income_out_file_handler
        self.main_window = main_window
        self.income_out_layout = [
            [sg.Text("Add the Title"), sg.InputText(key="-TITLE-")],
            [sg.Text("Add the Amount"), sg.InputText(key="-AMOUNT-")],
            [sg.Text("Select Category"), sg.Combo(values=self.category_data_manager.category_data_list, key="-CATEGORY-")],
            [sg.Button("Add Income"), sg.Button("Add Expense"), sg.Button("Close")],
        ]

    def open_data_window(self):

        data_window = sg.Window("Data", self.income_out_layout)
        event, values = data_window.read(timeout=5)
        data_window["-CATEGORY-"].update(values=self.category_data_manager.category_data_list)

        while True:
            event, values = data_window.read(timeout=5)

            if event == sg.WINDOW_CLOSED or event == "Close":
                break
            elif event == "Add Income":
                transaction_type = "In"
                self.user_data_manager.add_user_data_to_list(self.main_window, values, transaction_type)
                self.income_out_file_handler.save_to_json("user_data_file.json")
                self.user_data_manager.update_table(self.main_window)
                data_window["-TITLE-"].update("")
                data_window["-AMOUNT-"].update("")
            elif event == "Add Expense":
                transaction_type = "Out"
                self.user_data_manager.add_user_data_to_list(self.main_window, values, transaction_type)
                self.income_out_file_handler.save_to_json("user_data_file.json")
                self.user_data_manager.update_table(self.main_window)
                data_window["-TITLE-"].update("")
                data_window["-AMOUNT-"].update("")

        data_window.close()