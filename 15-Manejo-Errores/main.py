"""
    Capturar excepciones y manejar errores en código 
    susceptible a fallos/errores
"""

try:
    nombre = input("¿Cual es tu nombre): ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("Todo funciono correctamente")
finally: # Siempre se ejecuta el 'finally'
    print("Fin de la iteraccion")