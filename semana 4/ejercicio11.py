total_men = 0
total_women = 0
total_people = 6
counter = 1
while(counter <= total_people):
    number_user = int(input("Vamos a calcular el porcentaje de mujeres y hombres, ingrese un 1 para mujer o un 2 para hombre "))
    if(number_user == 1):
        total_women = total_women + 1
    else:
        total_men = total_men + 1
    counter = counter + 1
percent_of_men = total_men / total_people * 100 
percent_of_women = total_women / total_people * 100 
print(f"El porcentaje es de {percent_of_women}% mujeres y {percent_of_men}% hombres")


"""este lo intenté hacer con un ciclo for por lo de
saber el total de veces que el ciclo tenía que correr
pero al tener que usar operadores entre int y list para
sacar el porcentaje me dio error
"""