from exercise_5 import counting_upper_lower_cases

def test_counting_lower_and_upper_cases_working_properly():
    #Arrange
    input_string = "Testing the FUNCtion"
    #Act
    result = counting_upper_lower_cases(input_string)
    #Assert
    assert result == f"There's {5} upper cases and {13} lower cases"


def test_counting_lower_and_upper_cases_function_only_with_upper_case_letters():
    #Arrange
    input_string = "THIS IS AN UPPER CASE STRING ONLY"
    #Act
    result = counting_upper_lower_cases(input_string)
    #Assert
    assert result == f"There's {27} upper cases and {0} lower cases"


def test_counting_lower_and_upper_cases_function_only_with_lower_case_letters():
    #Arrange
    input_string = "this is a lower case string only"
    #Act
    result = counting_upper_lower_cases(input_string)
    #Assert
    assert result == f"There's {0} upper cases and {26} lower cases"