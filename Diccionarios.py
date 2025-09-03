#Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. 
#Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. 
#Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas.

#Creación y acceso
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"
#También puedes utilizar el método get() para obtener el valor de una clave. 
#Si la clave no existe, devuelve un valor predeterminado (por defecto, None).

#Métodos que se pueden usar en los diccionarios

#keys(): devuelve una vista de todas las claves del diccionario.
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])

#values(): devuelve una vista de todos los valores del diccionario.
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])

#items(): devuelve una vista de todos los pares clave-valor del diccionario.
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}