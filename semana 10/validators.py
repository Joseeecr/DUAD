import re

def validate_student_name_using_re(name):
    pattern = r'^[A-Za-z][A-Za-z ]*$'
    return re.match(pattern, name) is not None


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
    return re.match(pattern, grade) is not None