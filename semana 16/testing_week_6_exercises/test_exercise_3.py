from exercise_3 import sum_elements_list
import pytest

def test_sum_of_numbers_return_result_with_small_numbers():
    # Arrange
    input_list = [5,3,5,6,2]
    # Act
    result = sum_elements_list(input_list)
    # Assert
    assert result == 21


def test_sum_of_numbers_return_result_with_big_numbers():
    # Arrange
    input_list = [5000,332,5411,64,244]
    # Act
    result = sum_elements_list(input_list)
    # Assert
    assert result == 11051


def test_using_string_to_throws_exception():
    # Arrange
    input_string = "hello world"
    # Act/Assert
    with pytest.raises(TypeError):
        sum_elements_list(input_string)