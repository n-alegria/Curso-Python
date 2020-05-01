# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Interfaz grafica"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)

        ## Cambio en el tamaño de la ventana (ancho x alto)
        ## Bloquear redimensionar la ventana (horizontal, vertical) (utilizo 1=true - 0=false)
        ventana.geometry(self.size)
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)


        ## Comprobar si existe el archivo
        ruta_icono = os.path.abspath('./imagenes/ima.jpg')
        if os.path.isfile(ruta_icono):
            # Poner un icono en la ventana
            ventana.iconbitmap(ruta_icono)


        ## Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre (debe ser el ultimo metodo)
        self.ventana.mainloop()


# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("hola")
programa.addTexto("agregando texto")
programa.addTexto("desde metodos")
programa.mostrar()