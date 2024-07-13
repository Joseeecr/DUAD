import json

def reading_json_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found or doesn't exist")


def asking_pokemon_info():

    while True:
        pokemon_name = input("Insert the Pokemon's name ")
        if pokemon_name.isalpha():
            break
        else:
            print("Please use only letters for the Pokémon's name!")
    
    while True:
        pokemon_type = input("Insert the Pokemon's type ")
        if pokemon_type.isalpha():
            break
        else:
            print("Please use only letters for the pokemon's type!")

    while True:
        try:
            pokemon_hp = int(input("Insert the Pokemon's HP "))
            if pokemon_hp < 0:
                raise ValueError
            break
        except ValueError:
            print("Please use only positive numbers!")

    while True:
        try:
            pokemon_attack = int(input("Insert the Pokemon's attack strength "))
            if pokemon_hp < 0:
                raise ValueError
            break
        except ValueError: 
            print("Please use only positive numbers!")

    while True:
        try:
            pokemon_defense = int(input("Insert the Pokemon's defense points "))
            if pokemon_defense < 0:
                raise ValueError
            break
        except ValueError:
            print("Please use only positive numbers!")

    while True:
        try:
            pokemon_sp_attack = int(input("Insert the Pokemon's special attack strength "))
            if pokemon_sp_attack < 0:
                raise ValueError
            break
        except ValueError:
            print("Please use only positive numbers!")    
    
    while True:
        try:
            pokemon_sp_defense = int(input("Insert the Pokemon's special defense points "))
            if pokemon_sp_defense < 0:
                raise ValueError
            break
        except ValueError:
            print("Please use only positive numbers!")
    
    while True:
        try:
            pokemon_speed = int(input("Insert the Pokemon's speed "))
            if pokemon_speed < 0:
                raise ValueError
            break
        except ValueError:
            print("Please use only positive numbers!")

    pokemon_info = {
        "name": {
            "english": pokemon_name,
        },
        "type": [
            pokemon_type
        ],
        "base": {
            "HP": pokemon_hp,
            "Attack": pokemon_attack,
            "Defense": pokemon_defense,
            "Sp. Attack": pokemon_sp_attack,
            "Sp. Defense": pokemon_sp_defense,
            "Speed": pokemon_speed
        }
    }
    return pokemon_info


def main():
    try:
        file_path = "practicas_tarea_semana_8/json_practice/pokemons.json"
        pokemon_data = reading_json_file(file_path)
        
        new_pokemom = asking_pokemon_info()

        if len(pokemon_data) >= 4:
            pokemon_data[-1] = new_pokemom
        else:
            pokemon_data.append(new_pokemom)

        with open(file_path,"w") as file:
            json.dump(pokemon_data, file, indent= 4)

    except Exception as error:
        print(f"An unexpected error has occurred {error}")


if __name__ == "__main__":
    main()