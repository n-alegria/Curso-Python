# RETURN
# Devolver datos de una funcion

# Ejemplo 1
print("##### EJEMPLO 1 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

# Invocar funcion
print(saludame("Juan"))

# Ejemplo 2
print("##### EJEMPLO 2 #####")

def calculadora(numeroUno, numeroDos, basicas = False):
    suma = numeroUno + numeroDos
    resta = numeroUno - numeroDos
    multiplicacion = numeroUno + numeroDos
    division = numeroUno / numeroDos

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    cadena += "Multiplicacion: " + str(multiplicacion)
    cadena += "\n"
    cadena += "Division: " + str(division)
    cadena += "\n"
    return cadena

print(calculadora(2, 3, True))
print(type(calculadora(2, 4)))