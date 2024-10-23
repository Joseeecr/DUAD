import PySimpleGUI as sg
from sg_tables_logic import CategoryDataManager, UserDataManager
from files_handler import CategoryFileHandler, IncomeOutFileHandler
from GUIs import CategoryUI, IncomeOutUI

class MainWindowUI:

    def __init__(self):
        self.user_data_manager = UserDataManager()
        self.income_out_file_handler = IncomeOutFileHandler(self.user_data_manager)
        self.user_data_manager.user_data_list = self.income_out_file_handler.load_from_json("semana 17/user_data_file.json")
        self.category_data_manager = CategoryDataManager()
        self.category_file_handler = CategoryFileHandler(self.category_data_manager)
        self.category_data_manager.category_data_list = self.category_file_handler.load_from_json("semana 17/categories_file.json")
        
        if self.user_data_manager.user_data_list is None:
            self.user_data_manager.user_data_list = []

        self.headers = ["Title", "Category", "Type", "Amount"]
        self.layout = [
        [sg.Table(
            values=[list(data.values()) for data in self.user_data_manager.user_data_list],
            headings= self.headers,
            key= "-MAIN_TABLE-",
            auto_size_columns= False,
            col_widths= 20,
            justification= "center",
            enable_events=True
        )],
        [sg.Button("Add New Category"),  sg.Button("Add an income/expense"), sg.Button("Select row to delete", key="-DELETE_ROW-")]
    ]

    def opening_main_window(self):

        main_window = sg.Window("Income/Expense", self.layout)

        while True:
            event, values = main_window.read()

            if event == sg.WINDOW_CLOSED:
                break
            if event == "-DELETE_ROW-":
                self.income_out_file_handler.delete_item(values, main_window)

            elif event == "Add New Category":
                category_ui = CategoryUI(self.category_data_manager, self.category_file_handler)
                category_ui.open_category_window()
        
            elif event == "Add an income/expense":
                if not self.category_data_manager.category_data_list:
                    sg.popup("Please add at least one category before adding income/expense")
                    continue
                income_ui = IncomeOutUI(self.user_data_manager, self.category_data_manager, self.income_out_file_handler, main_window)
                income_ui.open_data_window()

        main_window.close()


if __name__ == "__main__":
    open_main_window = MainWindowUI()
    try:
        open_main_window.opening_main_window()
    except Exception:
        sg.popup("A random error occurred")