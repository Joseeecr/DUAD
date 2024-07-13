first_number = int(input("Ingrese su primer número "))
second_number = int(input("Ingrese su segundo número "))
third_number = int(input("Ingrese su tercer número "))
if(first_number + second_number + third_number == 30):
    print("Correcto")
elif(first_number == 30):
    print("Correcto")
elif(second_number == 30):
    print("Correcto")
elif(third_number == 30):
    print("Correcto")
else:
    print("Incorrecto")