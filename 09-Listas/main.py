"""
LISTAS (arrays)
    Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
    Para acceder a esos valores podemos usar un indice numerico.
    Se manejan por medio de sus indices siendo su primer elemento el de la posicion 0.
    Las listas pueden contener cualquier tipo de elemento, no hace falta que sea solo 'int' o 'string'
"""

pelicula = "Batman"

# Definir lista
# Se puede definir de 2 maneras, crearla directamente o mediante la funcion 'list()' a la cual hay que pasarle una 'tupla' para su creacion
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jenifer Lopez'))
year = list(range(2020, 2050))
variada = ["Nestor", 27, True, "Prueba"]

""" QUITAR PARA PRUEBA
print(pelicula)
print(peliculas)
print(cantantes)
print(type(cantantes))
print(year)
print(variada)
"""

# Indices
# Para acceder a una posicion se usan los indices siendo el 0 el primero, tambien se pueden usar indices negativos siendo el -1 el primero.
# Se puede seleccionar elementos mediante sus indices [desde : hasta]

print(peliculas[1])
print(peliculas[-1])
print(cantantes[0:2])
print(peliculas[1:]) # desde el 1 en adelante