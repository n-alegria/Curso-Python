numeros = [13, 64, 52, 73, 21, 7, 91, 63]

print("#"*10 + " Busqueda en la lista " + "#"*10)

# Introduzco dentro del 'try' el codigo que puede darme problemas
try:
    busqueda = int(input("Introduce el numero a buscar: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero a buscar: "))
    else:
        print(f"Has introducido {busqueda}")

    print("#"*3 + f"Buscar en la lista el numero {busqueda} " + "#"*3)

    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice: {search}")
# En el 'except' informo que ocurrio un error
except:
    print("El numero no esta en la lista") 