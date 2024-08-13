from validators import validate_student_name_using_re, validate_student_grade, validate_student_score

class Student:
    def __init__(self, student_name, student_grade, spanish_score, english_score, history_score, science_score, average_score):
        self.student_name = student_name
        self.student_grade = student_grade
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.history_score = history_score
        self.science_score = science_score
        self.average_score = average_score

    def __str__(self):
        return (f"Student= Name: {self.student_name}, Grade: {self.student_grade}, "
                f"Spanish: {self.spanish_score}, English: {self.english_score}, "
                f"History: {self.history_score}, Science: {self.science_score}, "
                f"Average: {self.average_score:.2f}")


def get_correct_student_name_or_grade(prompt, validator):
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


def add_new_student(student_list):
    while True:
        print("You chose to add a new student! Please fill the following fields with the required information:")
        student_name = get_correct_student_name_or_grade("Student name: ", validate_student_name_using_re)
        student_grade = get_correct_student_name_or_grade("Student grade: ", validate_student_grade)
        spanish_score = int(get_correct_input_score("Spanish score: ", validate_student_score))
        english_score = int(get_correct_input_score("English score: ", validate_student_score))
        history_score = int(get_correct_input_score("History score: ", validate_student_score))
        science_score = int(get_correct_input_score("Science score: ", validate_student_score))
        average_score = (spanish_score + english_score + history_score + science_score) / 4
        
        student_list.append(Student(student_name, student_grade, spanish_score, english_score, history_score, science_score, average_score))

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
    sorted_student_list = sorted(student_list, key= lambda student: student.average_score, reverse= True)
    if not sorted_student_list:
        print("There's nothing to show")
    else:
        for student in sorted_student_list:
            print(student.student_name, "=", student.average_score)


def get_overall_grade_score(student_list):
    overall_score_list = []
    for student in student_list:
        overall_score = student.average_score
        overall_score_list.append(overall_score)
    overall_score = sum(overall_score_list) / len(overall_score_list)
    print(f"The overall students' grade score is {overall_score}")