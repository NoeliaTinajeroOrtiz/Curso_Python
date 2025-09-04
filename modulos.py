#un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. 
#La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. 
#Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.

#Importar módulos

#Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. 
#Podemos importar un módulo completo o funciones específicas de un módulo.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
#En este ejemplo, se importa el módulo math utilizando la declaración import. 
#Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

#También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0
#En este caso, se importa solo la función sqrt() del módulo math, lo que nos permite utilizarla directamente sin tener que precederla con el nombre del módulo.

#Ejemplo de funciones y clases de módulos

import random #Ofrece funciones para generar números aleatorios
import datetime #Permite trabajar con fechas y horas

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

#Crear y utilizar módulos personalizados

#Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo

#Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py
#Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.

#Organización del código en módulos

#Es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. 
#Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.
#Al organizar nuestro código en módulos, podemos reutilizar funciones y mantener un código más estructurado y agrupado en módulos.

