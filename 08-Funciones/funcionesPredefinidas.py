nombre = "Nestor Alegria"

# Funciones generales
print(nombre)
print(type(nombre))

# Detectar el tipado
# Corroborar si es del tipo pasado como segundo parametro
# isinstance(object, type)

comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

# Limpiar espacios
frase = "   mi contenido    "
print(frase)
# Elimina espacios adicionales en el principio y el final de la cadena
print(frase.strip())

# Eliminar variables
year = 2020
print(year)
del year
# print(year) <- HABILITAR PARA PRUEBA

# Comprobar varaible vacia
texto = " ff "
if len(texto) > 0:
    print("No esta vacio")
    print(f"Tiene: {len(texto)} caracteres")
else:
    print("La varaible esta vacia")

# Encontrar caracteres, muestra la primer posicion donde comienza la variable en el texto
frase = "La vida es bella"
print(frase.find("vida"))

# Reemplazar palabra en string
nueva_frase = frase.replace("vida", "muerte")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(f"Mayuscula: {nombre.upper()}")
print(f"Minuscla: {nombre.lower()}")