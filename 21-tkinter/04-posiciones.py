from tkinter import *

ventana = Tk()
#ventana.geometry("500x500") -> Si no tengo indicada la medida de pantalla lo toma automaticamente mostrando todo el contenido

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg = "white", 
    bg = "black", 
    padx = 20, 
    pady = 50, 
    font = ("Consolas", 30), 
    )
texto.pack()

texto = Label(ventana, text="Soy lautaro")
texto.config(
    fg = "green",
    bg = "orange",
    font = ("Arial", 18),
    height = 2,
    cursor = "spider" 
    )
texto.pack(side = TOP)

texto = Label(ventana, text="basico")
texto.config(
    fg = "yellow",
    bg = "red",
    font = ("Arial", 18),
    height = 2,  
    cursor = "cross" 
    )
# SIDE = posicion <-> FILL = rellenar en X <-> EXPAND = permite expandir
texto.pack(side = TOP, fill = X, expand = YES)

texto = Label(ventana, text="basico")
texto.config(
    fg = "white",
    bg = "brown",
    font = ("Arial", 18),
    height = 2, 
    cursor = "cross" 
)
texto.pack(side = LEFT, fill = X, expand = YES)

texto = Label(ventana, text="basico")
texto.config(
    fg = "black",
    bg = "lightgreen",
    font = ("Arial", 18),
    height = 2, 
    cursor = "cross" 
    )
texto.pack(side = LEFT, fill = X, expand = YES)

texto = Label(ventana, text="basico")
texto.config(
    fg = "black",
    bg = "lightblue",
    font = ("Arial", 18),
    height = 2, 
    cursor = "cross" 
    )
texto.pack(side = LEFT, fill = X, expand = YES)

ventana.mainloop()