#Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos.
#Los elementos de una tupla se encierran entre paréntesis (), separados por comas.

#Creación y acceso
punto = (3, 4)

print(punto[0])  # Imprime 3

print(punto[1])  # Imprime 4

#A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. 
#No se pueden agregar, eliminar o cambiar elementos en una tupla existente.

#Métodos que se pueden usar en una tupla
mi_tupla = (1, 2, 3, 2, 4, 2)
#count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
print (mi_tupla.count(2)) #Salida: 3
#index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
print (mi_tupla.index(2))   # Salida: 1

print (mi_tupla.index(2, 2))   #Salida: 3

print (mi_tupla.index(2, 2, 4))   #Salida: 3
#len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
print (len(mi_tupla))