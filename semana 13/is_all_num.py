def print_parameters(func):
    def wrapper(*args):
        try:
            for number in args:
                int(number)
                print(number)
        except ValueError as ex:
            print(f"An error has been ocurred. Error : {ex}")
        func(*args)

    return wrapper

@print_parameters
def only_numbers(*args):
    pass



only_numbers(1,1,3,4,5,6)
only_numbers(1, "hello")