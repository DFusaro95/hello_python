
### SETS ###

'''
Un set es un tipo de dato que tiene de base una lista (array), es decir que al definirlo,
podemos agregarle datos completamente diferentes entre si sin afectar la estructura 
ni que nos de error. En python tenemos dos maneras de declarar un set:
'''

my_set = set() # Forma literal
my_other_set = {} # Forma intrinsica

# El problema con la forma intrinsica es que no se nos identifica como tal un 'set"
# Sino que en consola lo visualizaremos como un "Dictionary"

print(type(my_set)) # 'set'
print(type(my_other_set)) # 'dict'

'''
Al agregarle datos al set, veremos que efectivamente por consola deja de ser un 'dict' y
pasa a ser un 'set'
'''

my_other_set = {"Diego", "Fusaro", 29}
print(type(my_other_set)) # 'set'

# Supongamos que queremos aplicar las funciones intrinsicas de python en un set

print(len(my_other_set)) # Nos da como resultado un 3

# Ahora ¿Qué sucede cuando queremos acceder a uno de sus datos como si fuese una lista o tupla?

# print(my_other_set[1]) Podemos ver que esto nos da un 'TypeError'

# Sin embargo, dentro de un 'set' tenemos diferentes metodos que nos permiten manipularlos
# Asique antes de acceder a los elementos, veremos algunos metodos

my_other_set.add("Kaburt") # Añadimos un elemento con el metodo '.add'
print(my_other_set) # Visualizamos el set

'''
Al visualizar el set en consola nos damos cuenta de tres cosas, la primera es que efectivamente
nos ha agregado el dato que le indicamos, pero la segunda es que gracias a esto, sabemos que un 
set es MUTABLE a diferencia de las Tuples y la tercera, quizas la mas importante, estan todos
los datos desordenados. Por ende, podemos deducir que un set se diferencia en parte de una lista 
o tupla por la cualidad de que un set NO ES una estructura ordenada.
'''

# Intentemos agregar un dato nuevamente

my_other_set.add('Diego')
print(my_other_set)

'''
Lo que visualizamos aqui es que no solo sigue desordenado, sino que al agregarle el dato nuevamente,
este mismo, no se ha repetido indefinidamente de la cantidad de veces que lo agreguemos
'''

print('Diego' in my_other_set) # Intentamos buscar este elemento y nos responde un Boolean
print('Die' in my_other_set) # Lo mismo sucede aqui

my_other_set.remove("Diego")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

'''
Podemos mutar tambien el tipo de dato, lo cual no es recomendable ya que no sabemos 
en que orden quedaran los datos luego de la mutacion
'''

my_set = {"Diego", "Fusaro", 29}
my_list = list(my_set)
print(my_list) # Observamos el orden en el que quedo el set al mutarlo
print(my_list[0]) # Vemos que no coincide el numero del elemento

my_lang_set = {'Kotlin', 'Python', 'JavaScript'}
# Unificamos todos los valores en un solo set y volvemos a ver que no quedan ordenados
my_new_set = my_set.union(my_lang_set) 
print(my_new_set)

# Intentamos agregar nuevamente 'my_lang_set' y luego agregarle dos idiomas diferentes
print(my_new_set.union(my_lang_set).union({'Java', 'C++'}))
''' 
Lo que vemos es que al no admitir repetidos, no agrega nuevamente "my_lang_set" pero si 
agrega 'Java' y 'C++' incluso al no agregarlo al set como tal, sino, agregarlo al print
por ende nunca quedara guardado
'''

# Buscamos que diferencia entre esos dos sets
print(my_new_set.difference(my_lang_set)) 
# Vemos que imprime lo que no coincide entre esos dos sets