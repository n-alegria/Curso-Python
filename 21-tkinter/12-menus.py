from tkinter import *

ventana = Tk()
ventana.geometry("600x600")
# Creo un objeto del tipo 'Menu' y lo asocio a la ventana
mi_menu = Menu(ventana)
# Configuro el menu para que apareca en la vetana
ventana.config(menu=mi_menu)

# Submenu, indico que se agregara al menu principal 'mi_menu' y con 'tearoff' indico que no se vera la primer linea separadora
archivo = Menu(mi_menu, tearoff=0)
# Con 'add.command()' ingreso un nuevo renglon al menu
archivo.add_command(label = "Nuevo archivo")
archivo.add_command(label = "Nueva ventana")
# '.add_separator()' sirve ingresar un separador entre los menus
archivo.add_separator()
archivo.add_command(label = "Abrir archivo")
archivo.add_command(label = "Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

# Menu principal, con 'menu=archivo' agrego el submenu creado previamente
mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccionar")



ventana.mainloop()