from io import open
import pathlib

# Abrir archivo
# Se pueden usar rutas absolutas (con pathlib) o relativas
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo = open(ruta, "a+")

# Escribir dentro del archivo
archivo.write("Hola mundo\n")

# Cerrar archivo
archivo.close()
