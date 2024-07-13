import random
secret_number =  random.randint(1,10)
user_guess = int(input("Intenta adivinar el número del 1 al 10! "))
while(user_guess != secret_number):
    user_guess = int(input("Fallaste! Intentalo otra vez "))
print("Acertaste!")