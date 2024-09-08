
### Lists ###

'''
Las listas en Python nos permiten almacenar diferentes tipos de datos que poseemos en una misma variable.
podemos almacenar una cantidad infinita de elementos y tenemos dos maneras de definirlas. 
'''

my_list = list() # Forma numero 1
my_other_list = [] # Forma numero 2 (la mas utilizada)

print(len(my_list))

# Nuestra lista con datos
my_third_list = [35, 24, 62, 52, 30, 30, 17]
print(my_third_list)
print(len(my_third_list))

# Combinamos los datos
my_fourth_list = [29, 1.75, 'Diego', 'Fusaro', True]
print(type(my_fourth_list)) # Tipo de dato 'list'

# Accediendo a los datos

print(my_fourth_list[0]) # Pocisión 1 en la lista
print(my_fourth_list[1]) # Pocisión 2 en la lista
print(my_fourth_list[-1]) # Pocisión 1 comenzando desde el final (pocisión 4)
print(my_fourth_list[-4]) # Pocisión 4 comenzando desde el final (posición 1)
# print(my_fourth_list[4]) IndexError
# print(my_fourth_list[-5]) IndexError
print(my_third_list.count(30)) # Contamos la cantidad de veces que aparece el elemento indicado dentro de la lista

# Suma de listas

print(my_third_list + my_fourth_list)

# Las listas estan sujetas a modificaciones

print(my_other_list) # Lista vacia
my_other_list = 'Hello Python' # Asignamos el primer valor
print(my_other_list) 
my_other_list = 'Goodbye Python' # Asignamos el segundo valor
print(my_other_list) # Valor final

# Metodos de listas

my_fourth_list.append('diegofusarodev@gmail.com') # Agregamos un dato al final de la lista
print(my_fourth_list)
my_fourth_list.insert(3, 'Red') # Agregamos el dato en la pocisión indicada en el primer argumento
print(my_fourth_list)
my_fourth_list[3] = 'Green' # Reemplazo el dato en la pocision indicada
print(my_fourth_list)
my_fourth_list.remove('Green') # Eliminamos el dato indicado si se encuentra en la lista. Si hay mas de uno, elimina el primero que encuentra
print(my_fourth_list)
del my_fourth_list[2] # Elimina el elemento indicado entre corchetes 
print(my_fourth_list)
my_fourth_list.pop() # Eliminamos el ultimo dato de la lista
print(my_fourth_list)
my_fourth_list.pop(2) # Eliminamos el elemento en la pocisión indicada en el argunmento
print(my_fourth_list)
print(my_fourth_list[1:3]) #Mostramos el elemento que se encuentra entre los indices indicados

my_pop_element = my_fourth_list.pop(2) # Guardamos el elemento eliminado del 'pop()' en una variable
print(my_pop_element) # Mostramos en consola el elemento eliminado
print(my_fourth_list) # Lista de resultado final

my_copied_list = my_fourth_list.copy() # Copiamos la lista en otra variable para mantener los datos
print(my_copied_list)
my_copied_list.sort() # Ordenamos de la lista con criterio alfanumerico
print(my_copied_list)
my_copied_list.reverse() # Invertimos el sentido de la lista
print(my_copied_list)

my_fourth_list.clear() #Vaciamos la lista por completo
print(my_fourth_list)