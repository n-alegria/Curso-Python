from tkinter import *

main = Tk()
main.geometry("500x500")
main.config(
    bd = 50 # Borde transpatente de 50
)

# Primero debo crear 2 variables del tipo 'StringVar()'
# Para mostrar el dato debo almacenar el dato en una variable en este caso 'dato'
# Luego esa variable debo pasarla a la variable 'resultado' utilizando las funciones '.set()', utilizo una funcion para realizar esto
def getDato():
    resultado.set(dato.get())
    # Si los datos dentro del Label son mayores a 0 me cambia la configuracion
    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg = "green",
            fg = "white"
        )


dato = StringVar()
resultado = StringVar()


Label(main, text="Ingresa texto: ").pack(anchor=NW)
# Con 'textvariable' le indico en que variable almacenar el dato del 'Entry'
Entry(main, textvariable=dato).pack(anchor=NW)

Label(main, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(main, textvariable=resultado)
texto_recogido.pack(anchor=NW)
Button(main, text="Mostrar dato", command=getDato).pack(anchor=NW)

main.mainloop()