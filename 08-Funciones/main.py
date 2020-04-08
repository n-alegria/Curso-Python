"""
 FUNCIONES:
            una funcion es un conjunto de instrucciones agrupadas bajo
            un nombre concreto que pueden reutilizarse invocando a
            la funcion tantas veces como sea necesario.

        def nombreDeMiFuncion(paramatros):
            # BLOQUE / CONJUNTO DE INSTRUCCIONES

        nombreDeMiFuncion(parametros)
"""

# Ejemplo 1
print("##### EJEMPLO 1 #####")

def muestraNombres():
    print("Nestor")
    print("Lautaro")

# Invocar funcion
muestraNombres()

# Ejemplo 2
print("##### EJEMPLO 2 #####")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")

# Invocar funcion
mostrarTuNombre("Nestor", 27)

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
mostrarTuNombre(nombre, edad)

# Ejemplo 3
print("##### EJEMPLO 3 #####")

# Tabla de multiplicar con funcion
def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}\n")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
    print("\n")

# Invocar funcion
tabla(2)

# Ejemplo 3.1
# Tabla de multiplicar del 1 al 10
for numero_tabla in range(1,11):
    tabla(numero_tabla)