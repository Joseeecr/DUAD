def sum_of_numbers(num_1, num_2):
    return num_1 + num_2


def subtract_of_numbers(num_1, num_2):
    return num_1 - num_2


def multiply_of_numbers(num_1, num_2):
    return num_1 * num_2


def divide_of_numbers(num_1, num_2):
    return num_1 / num_2        


def making_calculations():
    current_number = 0
    while True:
        try:
            choosing_operator = int(input("""Ingrese un número para escoger que operacion quieres realizar! 
                                \n1= Suma \n2= Resta \n3= Multiplicación \n4= División \n5= Borrar resultado \n6= Salir \n"""))
            
            if choosing_operator <= 0 or choosing_operator > 6:
                raise ValueError
            
            if choosing_operator == 6:
                print("Saliendo del programa")
                break

            if choosing_operator == 5:
                current_number = 0
                print("Resultado borrado")
                continue
            
            if current_number == 0:
                numb_1 = int(input(f"Número actual = {current_number} Ingrese un nuevo número= "))
                numb_2 = int(input(f"Número actual = {numb_1} Ingrese otro número= "))
                
                if choosing_operator == 1:
                    sum_result = sum_of_numbers(numb_1, numb_2)
                    current_number = sum_result
                    print(f"El resultado de la suma de {numb_1} + {numb_2} es {sum_result}")
                    print()

                elif choosing_operator == 2:
                    subtract_result = subtract_of_numbers(numb_1, numb_2)
                    current_number = subtract_result
                    print(f"El resultado de la resta de {numb_1} - {numb_2} es {subtract_result}")
                    print()

                elif choosing_operator == 3:
                    multiply_result = multiply_of_numbers(numb_1, numb_2)
                    current_number = multiply_result
                    print(f"El resultado de la multiplicación de {numb_1} x {numb_2} es {multiply_result}")
                    print()

                elif choosing_operator == 4:
                    try:
                        divide_result = divide_of_numbers(numb_1, numb_2)
                        current_number = divide_result
                        print(f"El resultado de la división de {numb_1} / {numb_2} es {divide_result}")
                    except ZeroDivisionError:
                        print("No puedes divir entre 0")
                    print()
            else:
                if current_number != 0:
                    print(f"Número actual = {current_number}")
                    numb_2 = int(input(f" Ingrese otro número= "))

                    if choosing_operator == 1:
                        sum_result = sum_of_numbers(current_number, numb_2)
                        print(f"El resultado de la suma de {current_number} + {numb_2} es {sum_result}")
                        current_number = sum_result
                        print()

                    elif choosing_operator == 2:
                        subtract_result = subtract_of_numbers(current_number, numb_2)
                        print(f"El resultado de la resta de {current_number} - {numb_2} es {subtract_result}")
                        current_number = subtract_result
                        print()

                    elif choosing_operator == 3:
                        multiply_result = multiply_of_numbers(current_number, numb_2)
                        print(f"El resultado de la multiplicación de {current_number} x {numb_2} es {multiply_result}")
                        current_number = multiply_result
                        print()

                    elif choosing_operator == 4:
                        try:
                            divide_result = divide_of_numbers(numb_1, numb_2)
                            current_number = divide_result
                            print(f"El resultado de la división de {numb_1} / {numb_2} es {divide_result}")
                        except ZeroDivisionError:
                            print("No puedes divir entre 0")
                    print()
        except ValueError:  
            print("Ingrese un número válido!\n")


def main():
    try:
        making_calculations()
    except: Exception
    print("Ha ocurrido un error inesperado")

main()