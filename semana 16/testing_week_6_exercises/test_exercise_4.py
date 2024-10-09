from exercise_4 import reverse_string

def test_reverse_string_function_with_normal_string_result():
    #Arrange
    my_string = "Hello world!"
    #Act
    result = reverse_string(my_string)
    #Assert
    assert result == "!dlrow olleH"


def test_reverse_string_function_with_multiple_spaces():
    #Arrange
    multiple_spaces_string = "Hello         world"
    #Act
    result = reverse_string(multiple_spaces_string)
    #Assert
    assert result == "dlrow         olleH"


def test_reverse_string_function_with_empty_string():
    #Arrange
    empty_string = " "
    #Act
    result = reverse_string(empty_string)
    #Assert
    assert result == " "