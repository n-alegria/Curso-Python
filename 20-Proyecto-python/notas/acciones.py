import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}, vamos a crear una nueva nota...\n")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario.nombre}")

    def mostrar(self, usuario):
        print(f"\nVale, {usuario[1]}, aqui tienes tus notas\n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        print(f"--- NOTAS ---\n")
        for nota in notas:
            print(f"Titulo: {nota[2]}")
            print(f"Descipcion: {nota[3]}\n")
            print("-"*50+"\n")

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}, vamos a borrar notas")
        titulo = input("\nIntroduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] > 0:
            print(f"\nHemos borrado la nota: {nota.titulo}")
        else:
            print("\nNo se ha borrado la nota, prueba luego...")