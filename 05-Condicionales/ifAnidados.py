# Condicionales IF anidados

nombre = "Nestor"
ciudad = "Avellaneda"
continente = "America"
edad = 27
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "America":
        print("El usuario no es ameicano")
    else:
        print(f"Es americano y de ciudad {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")