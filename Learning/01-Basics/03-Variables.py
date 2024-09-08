# En esta clase veremos las variables y sus declaraciones.

my_str_variable = 'Hello World'
print(my_str_variable)

my_int_variable = 20
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Esta es la manera de imprimir multiples variables en la consola
# Debemos separar las distintas variables con comas ","
print(my_str_variable, my_int_variable, my_bool_variable)

# Con diferentes funciones integradas podemos hacer muchas cosas
# distintas. Sin ir mas lejos 'print()' o 'type()' son funciones
# integradas. Ahora veremos una mas:


# Con 'int()' podemos convertir un tipo de dato 'String' a 'Integer':

string_variable = '15' # Declaramos una variable tipo string
print(string_variable) # La imprimimos en consola
print(type(string_variable)) # Visualizamos su tipo de dato
to_number = int(string_variable) # Convertimos el tipo de dato a un Integer
print(type(to_number)) # Visualizamos su tipo de dato nuevamente


# Con 'str()' podemos convertir un tipo de dato 'Integer' a 'String':

number_variable = 30 # Declaramos una variable tipo integer
print(number_variable) # La imprimimos en consola
print(type(number_variable)) # Visualizamos su tipo de dato
to_string = str(number_variable) # Convertimos el tipo de dato a un String
print(type(to_string)) # Visualizamos el tipo de dato nuevamente


# Para saber cuantos caracteres tiene una variable:

print(len('Hello World'))


# En Python podemos declarar muchas variables con sus diferentes datos en 
# una sola linea de codigo y tambien podemos llamar a cada variable en un
# mismo print. Esto lo haremos de esta manera:

name, surname, alias, age = 'Diego', 'Fusaro', '0xBon', 29
print(f'My name is {name}, my surname is {surname}, Im known as {alias} and I have {age} years old')

# Esta sintaxis de declarar muchas variables juntas, si bien es posible 
# de realizar, no es una buena practica. No obstante, utilizar la sintaxis
# 'print(f'Este es mi nombre: {name}')' si es una buena practica.

# En python podemos capturar en una variable informacion de la consola 
# mediante la funcion integrada 'input()'. Con esta funcion le pediremos
#  al usuario de consola que nos proporcione su nombre para luego 
# nosotros saludarlo

first_name = input("what is your name: ")
print(f'Hello {first_name}, nice to meet you!')