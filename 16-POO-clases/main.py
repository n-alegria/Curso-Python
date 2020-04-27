# Programacion orientada a objetos (POO o OOP)

# --> Definir una clase (un molde para crear más objetos de ese tipo)

class Coche:

# --> Atributos o propiedades (caracteristicas del coche)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
# <-- Fin atributos
    
# --> Setter y getter
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocida
# <-- Fin Setter y getter

# --> Metodos
    # Metodos, acciones que hace el objeto coche (funciones)
    # --> Debo pasar siempre el parametro 'self' el cual se utilizara para llamar a los atributos
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
# <-- Fin metodos

# Fin definicion de la clase <-----

# --> Debo instanciar el objeto, no se usa la palabra 'new' simplemente se le asigna a la variable la clase a instanciar
coche = Coche()

print("Coche 1:")
print(coche) # Indica que es un objeto del tipo coche
print()
print(coche.marca) # Al ser un atributo publico me permite acceder y mostrarlo
print()

# Debo utulizar metodos setter y getter
coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(coche.marca, coche.getModelo(), coche.getColor())

print()
print(f"Velocidad actual: {coche.velocidad}")

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(f"Velocidad actual: {coche.velocidad}")

coche.frenar()
coche.frenar()

print(f"Velocidad actual: {coche.velocidad}\n")

# Crear mas objetos
coche2 = Coche()
print("Coche 2:\n")
coche2.setModelo("Gallardo")
coche2.setColor("Verde")
print(coche2.marca, coche2.getModelo(), coche2.getColor())
print(type(coche2))