from unittest_bubble_sort import bubble_sort 
import random
import pytest

def test_bubble_sort_with_small_list():
    # Arrange
    disordered_list = [4,5,2,3,6]
    # Act
    bubble_sort(disordered_list)
    #Assert
    assert disordered_list == sorted(disordered_list)


def test_bubble_sort_with_big_list():
    # Arrange
    input_list = list(range(0,200))
    random.shuffle(input_list)
    # Act
    bubble_sort(input_list)
    # Arrange
    assert input_list == sorted(input_list)


def test_bubble_sort_with_empty_list():
    # Arrange
    empty_list = []
    # Act
    bubble_sort(empty_list)
    # Assert
    assert len(empty_list) == 0


def test_bubble_sort_throws_exception_with_string():
    # Arrange
    input_list = "Some text"
    # Act/Assert
    with pytest.raises(TypeError):
        bubble_sort(input_list)