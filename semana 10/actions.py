import re

def validate_student_name_using_re(name):
    pattern = r'^[A-Za-z][A-Za-z ]*$'
    if re.match(pattern, name):
        return True 
    return  False


def validate_student_score(score):
    try:
        user_score = int(score)
        if user_score >= 0 and user_score <= 100:
            return user_score
        else: 
            print("Choose a number between 0 and 100!")
    except ValueError:
        print("Choose a number between 0 and 100!")


def validate_student_grade(grade):
    pattern = r'^\S+\s*\S$'
    if re.match(pattern, grade):
        return True 
    return  False


def get_correct_input_name(prompt, validator):
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        else:
            print("Write a valid option!")


def get_correct_input_score(prompt, validator):
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        else:
            continue


def get_correct_input_grade(prompt, validator):
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        else:
            print("Write a valid option!")


def add_new_student(student_list):
    while True:
        print("You chose to add a new student! Please fill the following fields with the required information:")
        student_name = get_correct_input_name("Student name: ", validate_student_name_using_re)
        student_grade = get_correct_input_grade("Student grade: ", validate_student_grade)
        spanish_score = int(get_correct_input_score("Spanish score: ", validate_student_score))
        english_score = int(get_correct_input_score("English score: ", validate_student_score))
        history_score = int(get_correct_input_score("History score: ", validate_student_score))
        science_score = int(get_correct_input_score("Science score: ", validate_student_score))
        average_score = (spanish_score + english_score + history_score + science_score) / 4

        student_information = {
        "name": student_name,
        "grade": student_grade,
        "spanish": spanish_score,
        "english": english_score,
        "history": history_score,
        "science": science_score,
        "average": average_score
        }
        student_list.append(student_information)

        while True:
            try:
                ask_user_if_repeat = int(input("Would you like to add another student? Type 1 for YES or 2 for NO "))
                if ask_user_if_repeat == 1:
                    break
                elif ask_user_if_repeat == 2:
                    return student_list
                else:
                    print("Choose a number between 1 and 2!")
                    continue
            except ValueError:
                print("Choose a number between 1 and 2!")


def sorting_student_best_scores(student_list):
    sorted_student_list = sorted(student_list, key= lambda student: student.get("average"), reverse= True)
    if not sorted_student_list:
        print("There's nothing to show")
    else:
        for student in sorted_student_list:
            print(student.get("name"), "=", student.get("average"))


def get_overall_grade_score(student_list):
    overall_score_list = []
    for student in student_list:
        overall_score = student.get("average")
        overall_score_list.append(overall_score)
    overall_score = sum(overall_score_list) / len(overall_score_list)
    print(f"The overall students' grade score is {overall_score}")