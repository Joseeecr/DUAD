contador = 1
suma = 0
user_number = int(input("Ingrese un número "))
while(contador <= user_number):
    suma = suma + contador
    contador = contador + 1
print(f"La suma de todos sus números da un total de {suma}")