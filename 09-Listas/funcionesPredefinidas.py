cantantes = ["Indio Solari", "Skay Beillinson", "Fernando Ruiz Diaz", "Ricardo Mollo"]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar listas

print(numeros)
numeros.sort()
print(numeros)

# Agregar elementos dentro de la lista
# Debo indicar en que indice se va a ingresar desplazando una posicion la lista restante
cantantes.append("Axel Rose")
cantantes.insert(1, "Dave Grohl")
print(cantantes)

# Eliminar elementos de la lista
# .pop(indice) -> elimina elementos de acuerdo a su posicion en el array
# .remove(nombre) -> elimina elementos de acuerdo a si esta o no en el array
cantantes.pop(1)
print(cantantes)
cantantes.remove("Indio Solari")
print(cantantes)

# Invertir lista
cantantes.reverse()
print(cantantes)

# Buscar dentro de la lista
# Retorna 'True' si esta en la lista 'False' si no esta

print("Indio Solari" in cantantes)
prueba = "Indio Solari" in cantantes
print(prueba)

# Contar elemento de la lista
# Debo usar la funcion len() pasando como argumento el nombre de la lista
print(len(cantantes))

# Cuantas veces aparece un elemento en la lista

print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

# Conseguir indice

print(f"Posicion en la lista: {cantantes.index('Axel Rose')}")

# Unir dos listas

cantantes.extend(numeros)
print(cantantes)

# Copiar lista

nueva_lista = cantantes.copy()
print(nueva_lista)


# Unir dos listas

tercerLista = cantantes + numeros
print(f"Tercer Lista:  {tercerLista}")


# Vaciar lista

numeros.clear()
print(numeros)