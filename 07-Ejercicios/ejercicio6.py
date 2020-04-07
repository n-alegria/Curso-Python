contador = 1
while(contador <= 10):
    print(f"\nTabla del {contador}\n")
    for i in range(1, 11):
        print(f"{contador} X {i} = {contador*i}")
    contador += 1