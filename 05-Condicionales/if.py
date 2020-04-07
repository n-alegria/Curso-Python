# Condicionales -> estructuras de control que me permite controlar el flujo del programa

# Condicional IF

"""
SI se_cumple_esta_condicion
    Ejecutar grupo de instrucciones
SI NO
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otra condicion
"""

# Ejemplo 1
# En el if no se usan ( ) ni { }
print("#################### EJEMPLO 1 ####################")

#color = "rojo"
color = input("Ingrese un color: ")
if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")