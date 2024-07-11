import csv

game_characteristics = [
    "name",
    "gender",
    "developer",
    "classification",
]

def asking_user_info():
    all_user_inputs = []
    while True:
        try:
            question_loop = int(input("Escriba 1 para juego, 2 para salir "))

            if question_loop != 1 and question_loop != 2:
                raise ValueError
            
            if question_loop == 2:
                print("Saliendo del programa")
                break

            if question_loop == 1:
                game_name = input("Ingrese el nombre de su juego ")
                game_gender = input("Ingrese el género de su juego ")
                game_developer = input("Ingrese el desarrollador de su juego ")
                game_classification = input("Ingrese la clasificación de su juego ")
                game_info = {
                    "name": game_name,
                    "gender": game_gender,
                    "developer": game_developer,
                    "classification": game_classification,
                }
                all_user_inputs.append(game_info)   
        except ValueError:
            print("Solo puedes escoger 1 o 2!")
            continue
    return all_user_inputs 


def writing_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding= "utf-8") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    try:
        writing_csv_file("practicas_tarea_semana_8/CSVs_practice/new_csv.csv", asking_user_info(), game_characteristics)
    except Exception:
        print("Ha ocurrido un error inesperado!")

main()