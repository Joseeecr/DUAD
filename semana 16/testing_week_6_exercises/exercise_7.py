def is_number_prime(number):
    if number <= 1:
        return False
    for check in range(2, number):
        if number % check == 0:
            return False
    return True


def filtering_prime_number(list_numbers):
    prime_numbers_list = []
    for number in list_numbers:
        if is_number_prime(number):
            prime_numbers_list.append(number)
    return prime_numbers_list

numbers = [1, 4, 6, 8, 9, 10]
range_of_numbers = list(range(0,101))
print(filtering_prime_number(numbers))