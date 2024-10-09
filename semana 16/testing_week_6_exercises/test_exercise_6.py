from exercise_6 import sorting_string_alphabetically

def test_sorting_string_function_working_properly():
    #Arrange
    my_string = "banana-apple-orange"
    #Act
    result = sorting_string_alphabetically(my_string)
    #Assert
    assert result == "apple-banana-orange"


def test_case_insensitive_string_sort():
    #Arrange
    my_string = "Banana-apple-Orange"
    #Act
    result = sorting_string_alphabetically(my_string)
    #Assert
    assert result == "apple-Banana-Orange"


def test_sort_function_string_with_special_characters_and_numbers():
    #Arrange
    string_with_characters_and_numbers = "apple-2-orange-1-banana-@watermelon"
    #Act
    result = sorting_string_alphabetically(string_with_characters_and_numbers)
    #Assert
    assert result ==  "1-2-@watermelon-apple-banana-orange"