from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

# Debo crear un objeto del tipo 'label' (Donde cargarlo, texto)
# Los puedo manejar a mi gusto -> 
# Siempre debo empaquetarlo
texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg = "white", # Color de letra
    bg = "black", # Color de fondo
    padx = 20, # Margen en x -> similar al padding en CSS
    pady = 50, # Margen en y -> similar al padding en CSS
    font = ("Consolas", 30), # Tipo de letra y tamaño
    )
texto.pack()

texto = Label(ventana, text="Soy lautaro")
texto.config(
    fg = "green",
    bg = "orange",
    font = ("Arial", 18),
    height = 2, # Alto de la caja -> no se calcula en porcentaje sino en cantidad de veces que se puede replicar el texto dentro de la caja
    cursor = "spider" # -> Cambia el cursor al posicionarse sobre la caja
    )
# Para posicionar el 'label' debo usar 'anchor' como parametro del pack con los puntos cardinales
texto.pack(anchor = E)

def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido} veo que eres de {pais}"

# Se puedo alterar los parametros pero funcionara de la misma forma
texto = Label(ventana, text=pruebas(pais="Argentina", nombre="nestor", apellido="alegria"))
texto.config(
    fg = "yellow",
    bg = "red",
    font = ("Arial", 18),
    height = 2, # Alto de la caja -> no se calcula en porcentaje sino en cantidad de veces que se puede replicar el texto dentro de la caja
    cursor = "cross" # -> Cambia el cursor al posicionarse sobre la caja
    )
# Para posicionar el 'label' debo usar 'anchor' como parametro del pack con los puntos cardinales
texto.pack(anchor = E)

ventana.mainloop()