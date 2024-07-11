def reading_file(path):
    try:
        with open(path) as file:
            songs = file.readlines()
        return [song.strip() for song in songs] 
    except FileNotFoundError:
        print("Ha ocurrido un error")


def saving_new_file(path, songs):
    with open(path, "w") as file:
        for song in songs:
            file.write(song + "\n")


def main():
    try:
        songs = reading_file("practicas_tarea_semana_8/txt_files_practice/list_of_songs.txt")
        print(songs)    
        sorted_songs = sorted(songs)
        saving_new_file("practicas_tarea_semana_8/txt_files_practice/new_list_of_songs.txt", sorted_songs)
    except Exception:
        print("Ha ocurrido un error inesperado")

if __name__ == "__main__":
    main()