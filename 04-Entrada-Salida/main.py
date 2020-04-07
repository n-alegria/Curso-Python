# Entrada
# Con el input ingreso string, si deceo ingresar numeros debo castearlo manualmenet

nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad?: ") # El dato ingresado es un string
numero = int(input("¿Cual es tu numero?: ")) # Casteo


# Salida
print(f"Hola {nombre}, tenes {edad}")
print(type(edad))
print(type(numero))