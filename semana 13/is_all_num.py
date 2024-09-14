def print_parameters(func):
    def wrapper(*args):
        if not all(isinstance(numb, (int, float)) for numb in args):
            raise TypeError("All parameters must be numbers!")
        return func(*args)
    return wrapper

@print_parameters
def only_numbers(*args):
    return args



print(only_numbers(1,1,3,4,5,6))
print(only_numbers(1, "hello"))