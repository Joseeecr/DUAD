from exercise_7 import filtering_prime_number

def test_filtering_prime_numbers_from_list_returns_only_primes():
    #Arrange
    list_of_numbers = [1, 4, 6, 7, 13, 9, 67]
    #Act
    result = filtering_prime_number(list_of_numbers)
    #Assert
    assert result == [7, 13, 67]


def test_filtering_prime_numbers_from_range_returns_only_primes():
    #Arrange
    range_of_numbers = list(range(0,101))
    #Act
    result = filtering_prime_number(range_of_numbers)
    #Assert
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def test_filtering_no_prime_numbers_returns_empty_list():
    #Arrange
    no_prime_numbers = [1, 4, 6, 8, 9, 10]
    #Act
    result = filtering_prime_number(no_prime_numbers)
    #Assert
    assert result == []