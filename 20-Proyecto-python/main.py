"""
Proyecto Python y Mysql
- Abrir asitente 
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identificará al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas, salir.
"""

# Desde el paquete 'usuarios' importar el modulo 'aciones.py'
from usuarios import acciones

print("""
Acciones disponibles:

1) Registro
2) Login
""")

# Creo un objeto del tipo 'Acciones' que contendra '.registro' y '.login()'
hazEl = acciones.Acciones()
accion = int(input("¿Que quieres hacer?: "))

if accion == 1:
    hazEl.registro()

elif accion == 2:
    hazEl.login()