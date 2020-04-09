
def holaMundo(nombre):
    return f"Hola {nombre}, como estas?"

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