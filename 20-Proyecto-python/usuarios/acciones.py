import usuarios.usuario as modelo

class Acciones:
    
    def registro(self):
        print("\nOK! Vamos a registrarte en el sistema...\n")
        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        # Instancio una clase del tipo 'Usuario'
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        if (registro[0] >= 1):
            print(f"\nPerfecto { registro[1].nombre} te has registrado con el mail {registro[1].email}\n")
        else:
            print("\nNo te has registrado correctamente\n")

    def login(self):
        print("\nOK! Identificate en el sistema...\n")    
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")