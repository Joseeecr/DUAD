def validating_user_menu_option(user_option):
        if user_option > 0 and user_option < 8:
            return True
        else:
            return False


def asking_user_which_menu_option():
    try:
        user_menu_option = int(input(
"""Choose one of the options:\n
1: Add a new student
2: View the current student list
3: View the top three scores of all students
4: View the overall grade score
5: Save all data into a CSV file
6: Load a current CSV file
7. Remove all students from the list\n"""))
        if validating_user_menu_option(user_menu_option):
            return user_menu_option
        else:
            print("Choose a number between 1 and 7")
    except ValueError:
        print("Choose a valid option!")