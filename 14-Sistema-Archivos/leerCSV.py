import pathlib, csv, operator
# Nombre archivo 'datos.csv' 

print("-> Lectura del .csv\n")

"""
# Abro el archivo con 'with' y le asigno unnombre con 'as'
print("Lectura basica del archivo\n")
with open("./14-Sistema-Archivos/datos.csv") as csvArchivo:
    lectura = csv.reader(csvArchivo)
    for registro in lectura:
        print(registro)
"""

"""
print("Lectura del archivo y realizar algunas funciones\n")
csvArchivo = open("./14-Sistema-Archivos/datos.csv") # Abro el archivo
lectura_archivo = csv.reader(csvArchivo) # Leo todos los registros
registro = next(lectura_archivo) # Leo el registro en formato de lista
print(registro) # Muestro el primer registro leido en formato lista
# identificacion, nombre, apellido, email, genero, direccionIp = next(lectura_archivo) # Leo el registro y le asigno los valores a las variables
# print(identificacion, nombre, apellido, email, genero, direccionIp) # Muestro los datos almacenados en las variables
# -> Aca voy leyendo linea por linea y asignando a las varaibles
identificacion, nombre, apellido, email, genero, direccionIp = next(lectura_archivo)
print(identificacion, nombre, apellido, email, genero, direccionIp)
identificacion, nombre, apellido, email, genero, direccionIp = next(lectura_archivo)
print(identificacion, nombre, apellido, email, genero, direccionIp)
del identificacion, nombre, apellido, email, genero, direccionIp # Borro los objetos (varaibles)
csvArchivo.close() # Cierro el archivo
del csvArchivo # Borro el achivo abierto
"""

"""
print("Lectura de archivo y ordenar lista")
csvArchivo = open("./14-Sistema-Archivos/datos.csv") # Abro el archivo
# operator.itemgetter(posicion) -> orden segun la posicion indicada por indice
# reverse = False -> indica si la lista se leera de forma inversa 
lista_ordenada = sorted(csvArchivo, key=operator.itemgetter(0), reverse=False)
print(lista_ordenada)
"""


print("Lectura sin libreria 'csv'\n")
archivo = open("./14-Sistema-Archivos/datos.csv", "r")
for linea in archivo:
    datos = linea.split(",")
    print(datos)
    print(datos[0]+"\t" +datos[1]+"\t"+datos[2])


print("\nUsando la libreria 'csv' nos muestra sin formato lista\n")
archivo = open("./14-Sistema-Archivos/datos.csv")
reader = csv.reader(archivo, delimiter=",")
for linea in reader:
    print(linea[0]+"\t" +linea[1]+"\t"+linea[2])