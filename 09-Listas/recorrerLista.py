# Recorrer el listado

peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jenifer Lopez'))
year = list(range(2020, 2050))
variada = ["Nestor", 27, True, "Prueba"]

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********** LISTADO DE PELICULAS **********")
for pelicula in peliculas:
    # .index(posicion) -> me da la posicion en el array de ese elemento
    print(f"{peliculas.index(pelicula)}. {pelicula}")