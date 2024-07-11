order_of_loop = [
    "primer numero ",
    "segundo numero ",
    "tercer numero ",
    "cuarto numero ",
    "quinto numero ",
    "sexto numero ",
    "septimo numero ",
    "octavo numero ",
    "noveno numero ",
    "decimo numero ",
]
number = 0
higher_number = 0
empty_list = []
for order in order_of_loop:
    number = int(input(f"Vamos a crear una lista de 10 números y encontraremos cuál es el mayor! Ingrese su {order}"))
    empty_list.append(number)
    if number > higher_number:
        higher_number = number
print(f"{empty_list} -> su número más alto fue {higher_number}")