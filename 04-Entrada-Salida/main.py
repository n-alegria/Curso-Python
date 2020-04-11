# Entrada
# Con el input ingreso string, si deceo ingresar numeros debo castearlo manualmenet

nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad?: ") # El dato ingresado es un string
numero = int(input("¿Cual es tu numero?: ")) # Casteo


print("*** SALIDA ***\n")
print(f"Hola {nombre}, tenes {edad}")
print(type(edad))
print(type(numero))


# Concatenacion
# Unir dos variables (string) -> se utliza el signo + para concatenar dos string
nombre = "Nestor"
apellido = "Alegria"
hobby = "Programador"
precio = 14.234

print(nombre + " " + apellido + " - " + hobby)

# Con la f"{}" puedo formatear directamente la varaible en el print -> debo utilizar {} y dentro el nombre de las varaibles
print(f"{nombre} {apellido} - {hobby}")

# Se puede concatenar de otras forma.
# Se utiliza la funcion ".format()", se debe usar { } donde quiero aplicar una variable y luego en el .format() escribo las variables en el orden de aparicion
print("Hola me llamo {} {} y mi hobby es {}".format(nombre, apellido, hobby))
print("Hola me llamo {variable1} {variable2} y mi hobby es {variable3}".format(variable1=nombre, variable2=apellido, variable3=hobby))
print("Hola me llamo {0} {1} y mi hobby es {2}".format(nombre, apellido, hobby))

# Le doy formato a la salida del float en maximo 2 decimales
print(f"EL precio es de {precio:.2f}")


