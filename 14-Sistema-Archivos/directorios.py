# Importo el modulo os
import os

# Crear una carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Copiar carpeta y su contenido
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./micarpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar carpeta
#os.rmdir("./mi_carpeta")

# Listar contenido carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
for fichero in contenido:
    print("Fichero: {0}".format(fichero))