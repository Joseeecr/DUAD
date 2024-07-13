user_number = int(input("Ingrese un número "))
if(user_number % 3 == 0 and user_number % 5 ==0):
    print("Fizzbuzz")
elif(user_number % 3 == 0):
    print("Fizz")
elif(user_number % 5 == 0):
    print("Buzz")
else:
    print("Su número no es divisible ni entre 3 ni entre 5")