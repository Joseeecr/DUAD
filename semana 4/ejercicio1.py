"""
'hola' + 3 = TypeError: can only concatenate str (not "int") to str

print('hola' + 'hola') -> holahola

'hola' + 'hola' -> no tira nada

3 + 'Hello' -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
list_one = [
    4,
    3,
    5,
    7
]
list_two = [
    7,
    6,
    3,
    3,
    5
]
print(list_one + list_two)

print(list_one + 'hello')
print(list_one + 4)

print(list_one + True)

print(13 + 11.1)
print(11.1 + 10.10)

print(False + True)
print(True + True)
print(False + False)
print(False + 5) 
print(False + "Hola")