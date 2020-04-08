# Ejemplo 1
print("##### EJEMPLO 1 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

print(getNombre("Nestor"), getApellido("Alegria"))


# Anido funciones, en una funcion global incluyo las de nombre y apellido
# asi en vez de llamarlas por separado las invoco llamando una unica funcion con los dos parametros
def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto
    

print(devuelveTodo("Nestor", "Fernandez"))