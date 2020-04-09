lista = [1, 12, 3, 53, 99, 6, 7, 2]

cadena = ""
print("1) Recorrer y mostrar la lista")
for numero in lista:
    cadena += str(numero) + "-"
print(cadena)

print("\n2) Ordenar y mostrar la lista")
lista.sort()
print(lista)

print(f"\n3) Tamaño de la lista: {len(lista)}")

print("\n4) Buscar algun elemento (que el usuario pida por teclado")
dato = int(input("Ingrese un numero: "))
if dato in lista:
    print(f"El numero {dato} esta en la lista")
else:
    print("No esta en la lista")

print("\nPuedo buscarlo por su indice")
search = lista.index(2)
print(f"El numero esta en el indice: {search}")