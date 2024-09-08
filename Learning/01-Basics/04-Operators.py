
### Operadores ###

'''
  En Python tenemos una extensa cantidad de operadores, 
  del tipo numericos y arigmeticos. En esta clase veremos 
  algunos ejemplos de los mas comunes y algunos mas 
  especificos para el uso de ciertas funcionalidades 
  del lenguaje.
'''

# Operadores Arigméticos

print(2 + 2) # Suma 
print(5 + 3) # Resta
print(3 * 4) # Multiplicación
print(5 / 11) # División
print(10 % 2) # Módulo
print(13 // 7) # Floor Division (redondea para abajo si da decimal)
print(2 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4) # Combinacion de todas


print('Hello ' + 'Python') # Concatenación
print('Hello  '+ str(5)) # Conversión + Concatenación
print('Hola ' * 5) # Multiplicación de Strings


# Operadores Comparativos

print(3 < 4) # Menor que
print(3 > 4) # Mayor que
print(3 <= 4) # Menor o igual que
print(3 >= 4) # Mayor o igual que
print(3 == 4) # Exactamente igual que
print(3 != 4) # Distinto que

print('Hello' < 'Python')
print('Hello' > 'Python')
print('aaaa' <= 'abaa') # Ordenación Alfabética por ASCII
print(len('Hello') >= len('Python')) # Conteo de Caracteres
print('Hello' == 'Python')
print('Hello' != 'Python') 

# Operadores Lógicos

print(3 < 4 and 'Hello' < 'Python') # True AND False = True
print(3 < 4 or 'Hello' < 'Python') # True OR False = True
print(3 > 4 and 'Hello' > 'Python') # False AND False = False
print(3 > 4 or 'Hello' > 'Python') # False OR False = False
print(not(3 < 4) and not('Hello' < 'Python')) # NOT True AND NOT True = False AND False = False
