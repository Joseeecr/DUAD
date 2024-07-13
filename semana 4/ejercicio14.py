order_of_loop = [
    "primer numero",
    "segundo numero",
    "tercer numero",
    "cuarto numero",
    "quinto numero",
]
higher_number = 0
for position_loop in order_of_loop:
    user_number = int(input(f"Ingrese el {position_loop} "))
    if(user_number > higher_number):
        higher_number = user_number
print(f"El número mayor es {higher_number}")