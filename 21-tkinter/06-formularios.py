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
encabezado.grid(row = 0, column = 0, columnspan = 20, sticky = W) # sticky = pegar al lado

# Label para el campo - Nombre
label = Label(ventana, text = "Nombre")
label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)

# Campo de texto - ingreso de informacion
# En lugar de usar '.pack()' puedo usar '.grid(fila, clumnda, padx, pady)'
campo_texto = Entry(ventana)
campo_texto.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
campo_texto.config(justify = "right", state = "normal") # state -> DISABLES (lo deshabilito)

# Label para el campo - Apellido
label = Label(ventana, text = "Apellido")
label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = W)
campo_texto = Entry(ventana)
campo_texto.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)
campo_texto.config(justify = "left", state = "normal") # justify -> me indica de que lado estará justificado el texto

# Label para el campo - Descripcion
label = Label(ventana, text = "Descripcion")
label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = NW)


# Campo de texto grande para la descripcion
campo_grande = Text(ventana)
campo_grande.grid(row = 3, column = 1)
campo_grande.config(
    width = 30,
    height = 5,
    font = ("Arial", 12),
    padx = 15,
    pady = 15
)


## Botones

# Añado un espaciado entre el 'Text' y el boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text = "Enviar")
boton.grid(row = 5, column = 1, sticky = W)
boton.config(
    padx=10,
    pady=10,
    bg="green",
    fg="white"
)

ventana.mainloop()