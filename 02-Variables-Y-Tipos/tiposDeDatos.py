# Tipo de dato que le podemos dar a una variable

# No tiene nada la variable
nada = None 
cadena = "Hola soy Nestor"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 100] #Coleccion de muchas variables
listaString = [44, "treinta", 30, "cuareta"]
tuplaNoCambia = ("master", "en", "python") 
diccionario = { # conjunto de Clave - Valor
    "nombre" : "Nestor",
    "apellido" : "Alegria",
    "hobby" : "Programar"
}
rango = range(9)
dato_byte = b"Probando"


# Imprimir variables
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)


# Mostrar tipo de dato -> en el print debo usar type() y dentro de parentesis la variable a averiguar el dato contenido
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(lista))
print(type(booleano))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

# Conversion de datos

texto = "Hola soy un texto"
numerito = 776
numero = 989
#print(texto + " " + numerito) -> da error, solo se puede concatenar string
# Se puede solucionar de dos maneras, parseando el dato a string
numerito = str(776) # asi
print(texto + " " + numerito)

# O directamente en el print
print(texto + " " + str(numero))