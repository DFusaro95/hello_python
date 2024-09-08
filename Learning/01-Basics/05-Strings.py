
### Strings ###

my_string = "My String"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "This is a \nnew line String"
print(my_new_line_string)

my_new_tab_string = "\tThis is a tabulated String"
print(my_new_tab_string)

my_scape_string = "\\tThis is a scaped \\n String"
print(my_scape_string)

# Format

'''
 Supongamos que los datos de nuestro software no los tenemos explicitamente,
 si no que vienen de un servidor. podemos tener las variables declaradas
 (en este ejemplo se encuentran los datos explicitos en las variables) y
 simplemente llamar a las distintas variables para poner dentro del string.
 ¿Como lo hacemos? tenemos la funcion ".format()" para hacerlo.
'''

name, surname, age = "Diego", "Fusaro", 29 # Variables

# Tenemos tres maneras: 

print("My name is {} {} and I have {} years old".format(name, surname, age)) # Utilizando la funcion '.format()'
print("My name is %s %s and I have %d years old" %(name, surname, age)) # Utilizando el formato con módulo '%'
print(f"My name is {name} {surname} and I have {age} years old") # Utilizando la letra 'f' de format antes de escribir el string (forma óptima)

# Desempaquetado de caracteres

language = 'python'
a, b, c, d, e, f = language

print(a)
print(b)
print(c)

# División de Strings
# Hay que tener en cuenta que en programación se comienza a contar a partir del 0

language_slice = language[1:3] # Tomamos caracteres del 1 al 3 sin contar el 3
print(language_slice)

language_slice = language[1:] # Tomamos caracteres del 1 al final del String
print(language_slice)

language_slice = language[-2] # Tomamos el segundo caracter del final hacia el principio
print(language_slice)

language_slice = language[1:2:4] # 
print(language_slice)

# Invertir

reversed_language = language[:: -1]
print(reversed_language)

# Funciones integradas

print(language.capitalize()) # Primer caracter en mayusculas
print(language.upper()) # Todo el String en mayúsculas
print(language.count('t')) # Conteo del caracter indicado dentro del String
print(language.lower()) # Todo el String en minúsculas
print(language.isnumeric()) # Verificamos si es numérico
print('1'.isnumeric()) # Verificamos si es numérico
print(language.upper().isupper()) # Pasamos el String a mayúsculas y luego verificamos si está en mayúsculas
print(language.upper().islower()) # Pasamos el String a minúsculas y luego verificamos si está en minúsculas
print(language.startswith('Py')) # Verificamos si el String comienza con los caracteres indicados
print('Py' == 'py') # Comparamos si los strings son iguales




