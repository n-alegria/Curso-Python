"""
    LISTAS MULTIMENSIONAL: listas dentro de listas

"""

print("********** CONTACTOS **********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

# Imprimir lista completa
print(f"Lista completa: {contactos}\n")

# Imprimir primer lista anidada
print(f"Primer contacto: {contactos[0]}")

# Seleccionar el elemento de la lista anidada
# lista[posicion de la lista anidada][posicion del elemento en la lista]
print(f"Email de {contactos[0][0]}: {contactos[0][1]}")

print()
# Imprime los contactos de forma individual
for contacto in contactos:
    print(contacto)

print()
# Imprime solo el nombre
for contacto in contactos:
    print(f"Nombre: {contacto[0]}")

print()
# Imprime los elementos de forma individual gracias al for anidado
for contacto in contactos:
    print()
    for elemento in contacto:
        print(elemento)

print()
# Imprime los elementos de forma individual gracias al for anidado
# El primer for separa las listas anidades en listas individuales
# El segundo for separa en elementos individuales los elementos dentro de las listas anidadas
for contacto in contactos:    
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print()
