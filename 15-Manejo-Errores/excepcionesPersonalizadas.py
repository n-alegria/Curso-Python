# Excepciones personalizadas o lanzar excepcion

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduzca la edad: "))

    # La palabra 'raise' se utiliza para generar una excepcion
    # La excepcion será almacenada en el error
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print("Bienvenido {}".format(nombre))
# Si la excepcion generada anteriormente es del tipo 'ValueError' ingresa acá
except ValueError:
     print("Introduce los datos correctamente.") 
except Exception as e:
    print("Existe un error", e)