from tkinter import *

ventana = Tk()
ventana.title("Master python")
ventana.geometry("700x700")

# --> Para pegar el contenido al borde superior o inferior debo usar 'anchor=N o anchor=S'

# Similar al 'div' de CSS
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg = "lightblue",
    # bd = 5, # Tamaño del borde
    # relief = "solid" # Tipo de relieve
)
marco_padre.pack(side = BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg = "red",
    bd = 5, # Tamaño del borde
    relief = "solid" # Tipo de relieve
)
marco.pack(side = LEFT, anchor = SW)
# Con '.pack_propagate(False)' evito que se propaguen sus caracteristicas
marco.pack_propagate(False)


Label(marco, text="Primer marco", bg="red", fg="white", font=("Arial", 20), bd=3, relief="solid", anchor=CENTER ).pack(fill=Y, expand=True)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg = "green",
    bd = 5, # Tamaño del borde
    relief = "solid" # Tipo de relieve
)
marco.pack(side = RIGHT, anchor = SE)


# Similar al 'div' de CSS
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg = "lightblue",
    # bd = 5, # Tamaño del borde
    # relief = "solid" # Tipo de relieve
)
marco_padre.pack(side = TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg = "blue",
    bd = 5, # Tamaño del borde
    relief = "solid" # Tipo de relieve
)
marco.pack(side = LEFT, anchor = NW)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg = "yellow",
    bd = 5, # Tamaño del borde
    relief = "solid" # Tipo de relieve
)
marco.pack(side = RIGHT, anchor = NE)

ventana.mainloop()