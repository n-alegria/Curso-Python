from tkinter import *
from tkinter import messagebox

def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

def sumar():
    resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado: ", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")
ventana.config(
    bd=25
)

marco = Frame(ventana, width=250, height=200)
marco.config(
    bd = 5,
    relief = SOLID,
    padx = 20,
    pady = 20
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(marco, text="Primer numero:").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()