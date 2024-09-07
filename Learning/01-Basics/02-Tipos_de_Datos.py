# Tipos de datos en Python:

'''
Python tiene diferentes tipos de datos, 
incluso mas que por ejemplo, Javascript, 
y para visualizar que tipo de dato es, 
debemos hacerlo mediante la consola con el 
comando 'Type'. Son estos:
'''

print(type(10)) # Tipo Integer
print(type(3.14)) # Tipo Float
print(type(1+ 3j)) # Tipo Complex
print(type('Hola Mundo')) # Tipo String
print(type([1, 2, 3])) # Tipo List (array en JS)
print(type({'nombre' : 'Diego', 'edad' : 25})) # Tipo Dictionary (objeto en JS)
print(type({9.8, 3.14, 2.7})) # Tipo Set
print(type((9.8, 3.14, 2.7))) # Tipo Tupla
print(type(print('¿Que tipo de dato es un print()?'))) # Tipo 'NoneType'