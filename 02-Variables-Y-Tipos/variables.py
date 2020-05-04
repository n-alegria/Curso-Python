"""
Una variables es un contenedor de informacion
que dentro guardara un dato, se puede crear
muchas variables y que cada una tenga un dato distinto
"""
# No hace falta declarar el tipo de dato (int, char, bool) ni cerrar la linea con ;
#Lenguaje debilmente tipado, si declaro dos veces la misma variable se quedara con la ultima declarada

# Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7
boolean = True

# Mostrar valor de lsa variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------")

# Sustituir el valor de alguns variables / reasignando valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("-------------------------------")

print("Con \'id()\' muestro la direccion de memoria donde se almacena la variable\n")
print(f"La variable 'texto' se almacena en {id(texto)}")