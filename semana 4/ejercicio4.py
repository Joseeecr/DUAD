numero_mayor = 0
contador = 1
total_intentos = 3
while(contador <= total_intentos):
    numero_usuario = int(input(f"Ingrese el número: número {contador} "))
    if(numero_usuario > numero_mayor):
        numero_mayor = numero_usuario
    contador = contador + 1
print(f"El número mayor es {numero_mayor}")