from tkinter import *

ventana = Tk()
ventana.title("Formularios")
ventana.geometry("700x400")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Lautaro Alegria")
encabezado.config(
    fg = "white",
    bg = "darkgray",
    font = ("Open Sans", 18),
    padx = 10,
    pady = 10
)
encabezado.pack(side = LEFT, anchor = NW, fill = X, expand = YES)


ventana.mainloop()