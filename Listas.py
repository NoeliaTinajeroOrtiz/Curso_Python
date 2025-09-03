#Crear la lista
frutas = ["manzana", "banana", "naranja"]

#Acceder a los elementos de la lista, siempre empiezan por 0
print("La lista contiene estos elementos: ")
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

#Acceder a los elementos de forma contraria con indices negativos
print("La lista contiene estos elementos en orden inverso: ")
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

#Métodos que se pueden usar en una lista

#append(elemento): agrega un elemento al final de la lista.
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

#insert(indice, elemento): inserta un elemento en una posición específica de la lista.
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

#remove(elemento): elimina la primera aparición de un elemento en la lista.
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

#pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

#sort(): ordena los elementos de la lista en orden ascendente.
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

#reverse(): invierte el orden de los elementos en la lista.
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

#Listas de compresión

#Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. 
#Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]