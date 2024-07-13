higher_number = 0
number_range = range(1, 101)
for number_list in number_range:
    number_user = int(input(f"Vamos a averiguar cuál es el número mayor entre 100 números! Ingrese el número: #{number_list} = "))
    if(number_user > higher_number):
        higher_number = number_user
print(f"El número mayor es {higher_number}")