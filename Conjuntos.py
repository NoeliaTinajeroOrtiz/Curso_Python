#Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos.
#Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().

#Creación
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

#Operaciones básicas
#Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

#Métodos que se pueden usar en los conjuntos

#add(elemento): agrega un elemento al conjunto.
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

#clear(): elimina todos los elementos del conjunto.
frutas.clear()
print(frutas)  # Imprime set()