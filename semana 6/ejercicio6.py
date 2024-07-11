def sorting_string_alphabetically(string):
    my_list = string.split("-")
    my_list.sort(key=str.lower)
    swap_to_string = "-".join(my_list)
    return swap_to_string


result = sorting_string_alphabetically("python-variable-funcion-computadora-monitor")

print(result)