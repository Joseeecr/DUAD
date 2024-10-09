from random import randint


def sum_elements_list(list_of_numbers):
    suma = 0
    for number in list_of_numbers:
        suma += number
    return suma


def main():
    list_of_numbers =  [randint(1,15) for number in range(0, 15)]
    print(f"Estos serán los números randoms que nos brinde la lista: {list_of_numbers}")
    print(f"Este es el resultado de la suma de esos números: {sum_elements_list(list_of_numbers)}")


main()