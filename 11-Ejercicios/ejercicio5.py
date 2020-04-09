tabla = [
    {
        'categoria': 'accion',
        'juegos': ['GTA', 'call of duty', 'pugb']
    },
    {
        'categoria': 'aventura',
        'juegos': ['assasins creed', 'crash bandicoot', 'principe de percia']
    },
    {
        'categoria': 'deportes',
        'juegos': ['fifa 21', 'pes 21', 'moto gp']
    }
]

# Recorro toda la tabla separando los diccionarios en elementos individuales
# Cada categoria es un diccionario individual
# Con categoria['categoria'] accedo al nombre de la categoria
# Con categoria['juegos'] accedo a la lista de juegos
for categoria in tabla:
    # Muestro el nombre de la categoria con la clave 
    print(f"--------------- {categoria['categoria']} ---------------")
    # Recorro la categoria separando la lista de juegos en elementos individuales
    for juego in categoria['juegos']:
        print(juego)