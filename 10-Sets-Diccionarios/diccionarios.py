"""
    DICCIONARIO: un tipo de dato que almacena un conjunto de datos.
    En formato clave - valor.
    Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Nestor",
    "apellido": "Alegria",
    "hobby": "Programar"
}

print(persona)
print(type(persona))
print()

# Para acceder debo usar el nombre de la clave
print(persona["apellido"])

# Lista con diccionarios

contactos = [
    {
        "nombre": "Lautaro",
        "email": "lautaro@lautaro.com"
    },
    {
        "nombre": "Luis",
        "email": "luis@luis.com"
    },
    {
        "nombre": "Salvador",
        "email": "salvador@salvador.com"
    }
]

print(contactos)

# Para acceder debo usar notacion de array
# variable[indice de la posicion][nombre de la clave]
print(contactos[0]['nombre'])

print("\nLista de contactos")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")