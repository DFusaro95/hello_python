
 ### Tuples ###

'''
Una tupla en Python es un conjunto de valores. 
No es lo mismo que una lista en cuanto a constructores. 
Las Listas llevan corchetes y las tuplas llevan parentesis.
'''

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (29, 1.75, 'Diego', 'Fusaro')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[6]) #IndexError
# print(my_tuple[-8]) #IndexError

print(my_tuple.count('Diego')) # Vemos cuantas veces en la tupla se repite ese elemento
print(my_tuple.index('Diego')) # Vemos en qué indice se encuentra el elemento en la tupla pero solo se queda con el primer elemento que encuentra

# my_tuple[1] = 1.90 # Intentamos modificar el valor del indice 1
# print(my_tuple) # TypeError

'''
Si bien una tupla tiene muy pocas opciones funcionales (solo posee count y index), una tupla es INMUTABLE a diferencia de las listas. 
por eso tiene tan pocas funciones integradas, ya que no es posible, una vez declarada la tupla, modificarla.
'''
my_other_tuple = (35, 26, 45, 'asd') # Declaramos la segunda tupla
my_sum_tuple = my_tuple + my_other_tuple # Intentamos juntar las dos tuplas declaradas
print(my_sum_tuple) # Vemos que si es soportado y ahora nuevamente, 'my_sum_tuple' es inmutable

print(my_sum_tuple[2:5]) # Vemos los datos que estan en el rango indicado contando el primer elemento pero no el ultimo
