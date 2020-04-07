numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))

suma = numeroUno + numeroDos
resta = numeroUno + numeroDos
multiplicacion = numeroUno * numeroDos
division = numeroUno / numeroDos

print(f"La suma es {suma}\nLa resta es {resta}\nLa multiplicacion es {multiplicacion}\nLa division es {division}")

# O tambien se puede realizar de la siguiente forma

print("Suma: " + str(numeroUno+numeroDos))
print("Resta: " + str(numeroUno-numeroDos))
print("Multiplicacion: " + str(numeroUno*numeroDos))
print("Division: " + str(numeroUno/numeroDos))