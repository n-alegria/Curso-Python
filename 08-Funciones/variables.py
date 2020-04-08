# Variables Globales y Locales
"""
 -> Una variable LOCAL se define dentro de la funcion y 
 solo es accesible dentro de la misma.
 A no ser que hagamos un return.
 -> Una variable GLOBAL se declara fuera de una funcion y
 esta disponible dentro y fuera de ella.
"""

"""
 LOCAL -> en el siguiente ejemplo existe una variable con el mismo nombre dentro 
 y fuera de la funcion. Aca me muestra el contenido de ambas variables ya que
 la funcion observa que dentro de ella hay una variable la cual es mas importante
 que la exterior
"""
frase = "Ni los genio son tan genios, ni los mediocres mediocres"
print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print(frase)

holaMundo()

"""
 GLOBAL -> en el siguiente ejemplo se imprime el contenido de 'texto' ya que no hay
 una variable dentro de la funcion con el mismo nombre por lo cual hara uso de
 la variable global.
 Tambien puedo convertir una variable LOCAL a GLOBAL, debo declarar la variable local de la siguiente manera:
 global website
 website = "google.com"
"""
texto = "Lorem Ipsum"
print(texto)

def muestraTexto():
    global website
    website = "google.com"
    print(f"Dentro: {website}")
    print(texto)

muestraTexto()
print(f"Fuera: {website}")