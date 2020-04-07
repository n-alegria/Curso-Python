numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))

if numeroUno < numeroDos:
    for i in range(numeroUno, numeroDos):
        print(f"{i}")
else:
    print("El primer numero debe ser menor al segundo numero")