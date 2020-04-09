"""
    SET tipo de dato, para tener una coleccion de valores pero no tiene indice ni orden.
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

print(personas)
print(type(personas))

# Agregar personas
personas.add("Carlos")
print(personas)

# Eliminar personas
personas.remove("Manolo")
print(personas)