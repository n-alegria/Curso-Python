peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jenifer Lopez'))
year = list(range(2020, 2050))
variada = ["Nestor", 27, True, "Prueba"]

# Indices
# Para acceder a una posicion se usan los indices siendo el 0 el primero, tambien se pueden usar indices negativos siendo el -1 el primero.
# Se puede seleccionar elementos mediante sus indices [desde : hasta]

print(peliculas[1])
print(peliculas[-1])
print(cantantes[0:2])
print(peliculas[1:]) # desde el 1 en adelante

# Se puede modificar el contenido de una posicion
print(f"Peliculas previas: {peliculas}")
peliculas[1] = "Gran Torino"
print(f"Peliculas posteriores: {peliculas}")