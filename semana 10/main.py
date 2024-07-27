from menu import asking_user_which_menu_option
from actions import add_new_student, sorting_student_best_scores, get_overall_grade_score
from data import save_data_as_csv_file, import_csv_file


def main():
    student_list = []
    while True:
        user_option = asking_user_which_menu_option()
        if user_option == 1:
            student = add_new_student(student_list)

        if user_option == 2:
            if not student_list:
                print("There's no students to show")
            else:
                for student in student_list:
                    print(student)

        if user_option == 3:
            sorting_student_best_scores(student_list)

        if user_option == 4:
            if not student_list:
                print("There's nothing to show")
            else:
                get_overall_grade_score(student_list)

        if user_option == 5:
            if not student_list:
                print("There's nothing to save")
            else:
                save_data_as_csv_file("semana 10/student_list.csv", student_list, student_list[0].keys())
                print("CSV file successfully saved as 'semana 10/student_list.csv'")

        if user_option == 6:
            try:
                student_list_from_csv = import_csv_file("semana 10/student_list.csv")
                student_list = student_list_from_csv
                print("CSV file successfully loaded")
            except FileNotFoundError:
                print("File doesn't exist")
        if user_option == 7:
            student_list.clear()
            print("All students were removed")
            continue


if __name__ == '__main__':
    main()