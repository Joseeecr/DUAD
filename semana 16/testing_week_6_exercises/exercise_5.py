def counting_upper_lower_cases(string):
    counter = {"upper_cases": 0, "lower_cases": 0,}
    for character in string:
        if character.isupper():
            counter["upper_cases"] += 1
        elif character.islower():
            counter["lower_cases"] += 1
    return f"There's {counter['upper_cases']} upper cases and {counter['lower_cases']} lower cases"


counting_upper_lower_cases("THIS IS AN UPPER CASE STRING ONLY")