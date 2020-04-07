"""
# FOR -> estructura iteractiva que se repetira X cantidad de veces
for 'varaible' in 'elemento_iterable' (lista, rango, tupla, etc)
    BLOQUE DE INSTRUCCIONES

Se puede anidar if dentro del
"""
contador = 0
resultado = 0
for contador in range(0, 10):
    print("Voy por el " + str(contador)) # Casteo el contador (int) a string para poder concatenarlo
    resultado = resultado + contador

print(f"El resultado es: {resultado}")

print("***** TABLA DE MULTIPLICAR *****")

numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

for numero_tabla in range(1, 11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")
