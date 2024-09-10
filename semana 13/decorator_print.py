def print_parameters(func):
    def wrapper(*args):
        if len(args) == 1:
            print(f"These were the parameters: {args[0]}")
        else:
            print(f"These were the parameters: {args}")

        result = func(*args)
        print(f"The return is: {result}")
        return result

    return wrapper

@print_parameters
def sum_of_numbers(numb1, numb2, numb3, numb4):
    return numb1 + numb2 + numb3 + numb4


@print_parameters
def writing_text(string):
    return string


writing_text("This is a test")


sum_of_numbers(1, 3, 99, 33)