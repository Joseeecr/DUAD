import pytest
from validators import Validators

def test_validate_user_input_with_expected_input():
    #Arrange
    user_input = "Salary"
    #Act
    result = Validators.validate_user_input(user_input)
    #Assert
    assert result == True


def test_validate_user_input_with_wrong_input():
    #Arrange
    user_input = "124"
    #Act
    result = Validators.validate_user_input(user_input)
    #Assert
    assert result == False