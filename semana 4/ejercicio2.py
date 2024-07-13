person_name = input("Ingrese su nombre ")
person_last_name = input("Ingrese su apellido ")
person_age = int(input("Ingrese su edad "))
if (person_age < 0):
	print("Edad invalida")
elif(person_age <= 3):
    print(f"{person_name} {person_last_name} es un bebé")
elif(person_age <= 10):
    print(f"{person_name} {person_last_name} es un niño")
elif(person_age <= 18):
    print(f"{person_name} {person_last_name} es un preadolescente")
elif(person_age <= 26):
    print(f"{person_name} {person_last_name} es un adulto joven")
elif(person_age <= 59):
    print(f"{person_name} {person_last_name} es un adulto")
else:
    print(f"{person_name} {person_last_name} es adulto mayor")