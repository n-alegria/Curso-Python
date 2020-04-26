# Multiples excepciones #

# Introduzco el codigo que puede producir un error dentro del 'try'
try:
    numero = int(input("numero para elevar al cuadrado:"))
    print("El cuadrado es: " + str(numero*numero))
# Manejo los posibles errores de forma independiente
# --> 'TypeError' - Error del tipo de dato
except TypeError:
    print("Debes convertir tus cadenas a enteros.\n")
# --> 'ValueError' - Error en el ingreso de dato (str)
except ValueError:
     print("Debes ingresar un numero.\n")
# Tambien puedo capturar los errores en variables para mostrarlas por pantalla
except Exception as e: 
    print("Ha ocurrido un error: '" + type(e).__name__ + "'")