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

# Concatenacion
# Unir dos variables (string) -> se utliza el signo + para concatenar dos string
nombre = "Nestor"
apellido = "Alegria"
hobby = "Programador"

print(nombre + " " + apellido + " - " + hobby)

# Con la f"{}" puedo formatear directamente la varaible en el print -> debo utilizar {} y dentro el nombre de las varaibles
print(f"{nombre} {apellido} - {hobby}")

# Se puede concatenar de otra forma.
# Se utiliza la funcion ".format()", se debe usar { } donde quiero aplicar una variable y luego en el .format() escribo las variables en el orden de aparicion
print("Hola me llamo {} {} y mi hobby es {}".format(nombre, apellido, hobby))