from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showwarning("Alerta", "Soy el papa")

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()


def salir(nombre):
    # Puedo asignar el retorno a una variable y usarla para ejercer control sobre la iteraccion
    resultado = MessageBox.askquestion("Salir", "¿Continuar?")
    if resultado != "yes":
        MessageBox.showinfo("Chau", f"Adios para siempre {nombre}")
        ventana.destroy()

# Debo usar funciones 'lambda' para usar funciones con parametros
Button(ventana, text="Salir", command= lambda: salir("Lautaro")).pack()


ventana.mainloop()