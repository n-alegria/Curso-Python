diccionario = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}

print("*** Cambiar valores ***\n")
print("Se debe igualar la clave con el nuevo valor")
diccionario['year'] = 1980

print("*** Recorrer un diccionario ***\n")
# Muestro de acuerdo a la clave, la cual se almacenara en 'x' 
# y con ella muestro el valor que posee con esa clave en el diccioanrio
for x in diccionario:
    print(f"La clave es: '{x}' y el valor es: '{diccionario[x]}'")
    print()

# Puedo almacenar clave valor en 2 variables utilizando el metodo '.items()'
for x,v in diccionario.items():
    print(f"La clave es: '{x}' y el VALOR es: '{v}'")
    print()

print("*** Comprobar si existe la clave ***\n")
if 'model' in diccionario:
    print("Si, 'model' es una de las llaves del diccionario")

print("*** Longitud del diccionario ***\n")
print(len(diccionario))

print("*** Adicion de elementos ***\n")
print("Debo declarar la nueva llave e igualarla con el nuevo valor")
diccionario["color"] = "rojo"

print("*** Eliminar elementos ***\n")
print(" Existen varios metodos para eliminar elementos")
# El .pop() elimina el elemento con su clase especifica
diccionario.pop("model")

# El .popitem() elimina el ultimo elemento del diccionario
diccionario.popitem()

# La palabra 'del' elimina un elemento con el nombre de clave espedificada.
# Tambien sirve para eliminar por completo el diccionario del (diccionario)
del diccionario["year"]

print("*** Copiar un elemento ***\n")
nuevo_diccionario = diccionario.copy()


print("*** Diccionarios anidados ***\n")
miFamilia = {
    "chicoUno": {
        "nombre": "nestor",
        "anio" : 2004
    },
    "chicoDos": {
        "nombre": "lautaro",
        "anio" : 2020
    },
    "chicoTres": {
        "nombre": "sebastian",
        "anio" : 2010
    }
}
print(miFamilia)
print(f"\nSegundo chico: {miFamilia['chicoDos']}")


print("*** Constructor 'dict()' ***\n")
print("Es posible utilizar el 'dict()' como constructor para hacer un nuevo diccionario")
thisDict = dict(breand="Ford", model="Mustang", year=1964)
print(thisDict)