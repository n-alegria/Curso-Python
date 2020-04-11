mi_texto = "Master"
mi_texto2 = "en Python"

# Concatenar en una nueva variable
texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# Si quiero usar un texto entre comillas debo usar un caracter de escape \
mi_texto3 = "hola \"Mundo\""
print(mi_texto3)

# Tambien se puede usar comillas simples para usar dobles o dobles para usar simples
mi_texto4 = "'Saltamontes'"
print(mi_texto4)

# Puedo imprimir caracteres individuales de los string con la posicion que deseo imprimir
print(f"Imprimo el primer caracter de la varaible: {mi_texto[0]}")

"""
 \n -> Salto de linea
 \t -> tabulacion
 \r -> elimina todo lo anterior al caracter de escape
"""

# Para evitar los caracteres especiales debo usar 'r' delante del texto a imprimir
print(r"C:\nombre\directorio")

print("*** Operaciones ***")
# Esposible ralizar operaciones entre string
textoA = "Esto es una cadena"
textoB = "Y esta es otra distinta"

# Suma de string
print(textoA + textoA)
print("Hola mundo" + textoA)

# Multiplicacion de cadenas
diez_espacios = " " * 10
print(diez_espacios + textoB)

# Imprimir partes del string
print(textoA[1:4])

