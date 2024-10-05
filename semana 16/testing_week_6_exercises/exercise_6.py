def sorting_string_alphabetically(string):
    my_list = string.split("-")
    my_list.sort(key=str.lower)
    swap_to_string = "-".join(my_list)
    return swap_to_string


result = sorting_string_alphabetically("apple-2-orange-1-banana-@watermelon")

print(result)