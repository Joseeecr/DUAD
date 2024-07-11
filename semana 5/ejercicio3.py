from random import randint
list_random = [randint(1,15) for number in range(0, 15)]
print(f"List before swaping {list_random}")
list_random[0], list_random[-1] = list_random[-1], list_random[0]
print(f"List after swaping {list_random}") 