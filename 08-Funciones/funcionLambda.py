# Funciones Lambda
"""
 Es una funcion anonima, no tiene nombre concreto y no hace falta definirla con el def, nombre y parametros
 Son funciones que sirven para tareas pequeñas pero repetitivas
 
 Se crean de la siguiente forma:
 Primero se aplica un nombre a la funcion, luego se agrega el signo igual y la palabra reservada 'lambda'
 y luego se define el parametro y un retorno entre ':'
"""

# Creacion de la funcion
dime_el_year = lambda year: f"El año es {year}"

# Invocacion de la funcion
print(dime_el_year(2021))