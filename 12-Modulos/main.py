"""
    MODULOS: son funcionalidades ya hechas para reutilizar.
    En python hay muchos modulos.

    Podemos conseguir modulos que ya vienen en el lengaje,
    modulos en internet y tambien crear propios.
"""

# Importar modulo propio completo con todas sus funciones
# Se utiliza como un objeto miModulo.holaMundo('nombre')
#import miModulo
"""
print(miModulo.holaMundo("Lautaro"))
print()
print(miModulo.calculadora(3, 5, True))
"""

# En caso de querer llamar solo a una funcion del modulo uso
#from miModulo import holaMundo
"""
print(miModulo.holaMundo("Lautaro"))
print()
"""

# En el caso de no querer manejarlo como objeto debo hacer
from miModulo import *

print(holaMundo("Lautaro"))
print()
print(calculadora(3, 5, True))