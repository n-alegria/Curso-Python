numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))

if numeroUno < numeroDos:
    for i in range(numeroUno, numeroDos):
        if i%3 == 0:
            print(f"El numero {i} es impar")
