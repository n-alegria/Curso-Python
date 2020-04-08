# Parametros opcionales
# Se establece igualando el parametro en la firma de la funcion al valor en el cual quiero iniciar la variable
# Adicionalmente en la funcion se puede comprobar con un 'if' si existe el parametro lo muestro de lo contrario no

# Ejemplo 1
print("##### EJEMPLO 1 #####")

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Juan")
getEmpleado("Lautaro", 27)