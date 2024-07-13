import random
secret_number = random.randint(1,10)
user_guess =  int(input("Intenta adivinar el número secreto! Ingresa un número del 1 al 10 "))
while(user_guess != secret_number):
     user_guess = int(input("Fallaste! Intenta otra vez "))
print("Acertaste el número correcto!")

""" 
Había leído que la función random creaba numeros al azar, solo tuve 
que buscar la manera de implementarlo bien en el código
"""