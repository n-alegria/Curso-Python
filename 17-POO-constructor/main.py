# Importo la clase Coche o puedo hacer 'import coche' pero debo usar notacion static 'coche.Coche'
from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Acul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 150, 200, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
carro3 = 23
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

# Visibilidad
# --> publicos (por defecto) - privados '__nombreVariable'

print(carro.soy_publico)
print(carro.getPrivado())