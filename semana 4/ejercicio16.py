counter = 1
addition_of_numbers = 0
while(counter <= 100):
    user_number = int(input(f"Vamos a sumar 100 números, ingrese el número: #{counter} "))
    addition_of_numbers = addition_of_numbers + user_number
    counter = counter + 1
print(f"La suma total de sus 100 números es {addition_of_numbers}")