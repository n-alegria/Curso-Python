import usuarios.usuario as modelo
import notas.acciones

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
        try:   
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            # Creo al usuario y paso los campos 'nombre' y 'apellido' vacios
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\nBienvenido {login[1]} te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"\nLogin incorrecto, intentalo nuevamente")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:

        - Crear Notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!")
            exit()