from io import open
import pathlib
"""
    La funcion 'open()' toma dos parametros; nombre de archivo y modo.
    Existen cuatro diferentes metodos (modos) para abrir un archivo:

        "w" - Lectura -> Valor por defecto. Abre un archivo para lectura, da error si el archivo no existe.
        "a" - Agregar -> Abre un archivo para agregar, crea el archivo si no existe.
        "w" - Escritura -> Abre un archivo para escribir, crea el archivo si no existe.
        "x" - Crear -> Crea un archivo especifico, da error si el archivo no existe.

    Ademas, se le puede especificar si el archivo deberia manejarse en modo binario o texto.

        "t" - Texto -> Valor por defecto. Modo texto.
        "b" - Binario -> Modo Binario (ej. imagenes)
"""
# Abrir archivo
# Se pueden usar rutas absolutas (con pathlib) o relativas
print("***** Abrir archivo para adicionar *****\n")
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo = open(ruta, "a+")

# Escribir dentro del archivo
archivo.write("Hola mundo\n")

# Cerrar archivo
archivo.close()

# Se pueden usar rutas absolutas (con pathlib) o relativas
print("***** Abrir archivo para leer *****\n")
print("-> Lectura completa")
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo_lectura = open(ruta, "r")

contenido = archivo_lectura.read()
print(contenido)
archivo.close()

# Leer contenido y guardarlo en una lista
print("-> Lectura en forma de lista")
ruta = str(pathlib.Path().absolute()) + "/ficheros.txt"
archivo_lectura = open(ruta, "r")

lista = archivo_lectura.readlines()
print("Contenido de la lista: \n")
print(lista)

# Leer contenido y guardarlo en una lista
print("-> Copiar, renombar y borrar archivo")
# Importamos el modulo
import shutil

# -> Copiar -> de la original a la nueva
"""
ruta_original = str(pathlib.Path().absolute()) + "/ficheros.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

# Copiare el archivo en otro directorio
ruta_alternativa = "./08-Funciones/fichero_texto_nuevo.txt"
ruta_alternativa_nueva = str(pathlib.Path().absolute()) + "/./07-Ejercicios/fichero_copiado.txt"

shutil.copyfile(ruta_original, ruta_alternativa_nueva)
"""

# -> Mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-Sistema-Archivos/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# -> Eliminar -> hay que importar el modulo os
"""
import os
ruta = str(pathlib.Path().absolute()) + "/08-Funciones/fichero_texto_nuevo.txt"
os.remove(ruta)
"""

# -> Comprobar si el archivo existe
import os
existe = os.path.abspath("./")
print(existe)
print(os.path.abspath("../"))

# Se puede hacer de varias formas

# Primera ->
#   ruta_comprobar = os.path.abspath("./") + "/ficheros.txt"
#   print(f"Ruta: {ruta_comprobar}")

# Segunda ->
if os.path.isfile(os.path.abspath("./") + "/ficheros.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")
    