global_variable = 50

def variable_inside_function(global_variable):
    var_to_practice = "Hello"
    print(f"Aquí sí va a servir, esta es mi variable local: {var_to_practice}")
    print(global_variable)


variable_inside_function(True)
print(f"Esto es un print de la variable global: {global_variable}")
# print(f"Aquí no va a funcar {var_to_practice}")