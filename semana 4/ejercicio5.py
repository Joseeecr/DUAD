contador = 1
total_notas = int(input("Bienvenido! Ingrese el número total de notas a calcular "))
notas_aprobadas = 0
notas_desaprobadas = 0
promedio_notas_aprobadas = 0
promedio_notas_desaprobadas = 0 
while(contador <= total_notas):
    notas = int(input(f"Ingrese la nota número {contador} "))
    if(notas>= 70):
        notas_aprobadas = notas_aprobadas + 1
        promedio_notas_aprobadas = promedio_notas_aprobadas + notas
    else:
        notas_desaprobadas = notas_desaprobadas + 1
        promedio_notas_desaprobadas = promedio_notas_desaprobadas + notas
    contador = contador + 1
porcentaje_notas_aprobadas = promedio_notas_aprobadas / notas_aprobadas 
porcentaje_notas_desaprobadas = promedio_notas_desaprobadas / notas_desaprobadas 
promedio_total = (promedio_notas_aprobadas + promedio_notas_desaprobadas) / total_notas
print(f"Su total de notas aprobadas es {notas_aprobadas}")
print(f"Su total de notas desaprobadas es {notas_desaprobadas}")
print(f"Su promedio de notas aprobadas es {porcentaje_notas_aprobadas}")
print(f"Su promedio de notas desaprobadas es {porcentaje_notas_desaprobadas}")
print(f"Su promedio total es {promedio_total}")