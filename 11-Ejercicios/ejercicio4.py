lista = ["hola", 12]
texto = "Mundo"
numero = 90
verdadero = True

def traducirTipo(tipo):
    resultado = None
    if tipo == list:
        resultado = "Lista"
    elif tipo == "str":
        resultado = "CADENA DE TEXTO"
    elif tipo == int:
        resultado == "NUMERO ENTERO"
    elif tipo == bool:
        resultado = "BOOLEANO"
    return resultado


def comprobarDato(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        print(f"Este dato es del tipo {traducirTipo(tipo)}")
    else:
        result = None
    return result

print(comprobarDato(lista, list))