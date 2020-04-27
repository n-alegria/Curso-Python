class Coche:

# --> Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Para indicar que un atributo es privado debo poner antes del nombre '__' y acceder a él desde mi clase utilizando 'get' y 'set'
    soy_publico = "Soy un atributo publico"
    __soyPrivado = "Soy un atributo privado"
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
        return self.velocidad

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def getPrivado(self):
        return self.__soyPrivado
# <-- Fin Setter y getter

# --> Constructor
    # '__init__' define el constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
# <--

# --> Metodos
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getInfo(self):
        info = "--- Informacion del coche ---"
        info += "\nColor: " + self.getColor()
        info += "\nMarca: " + self.getMarca()
        info += "\nModelo: " + self.getMarca()
        info += "\nVelocidad: " + (str)(self.getVelocidad())
        info += "\nPlazas: " + (str)(self.getPlazas())
        info += "\n"
        return info
# <-- Fin metodos

"""
    Se puede eliminar atributos de la instancia utilizando: 'del carro.color'
    Se puede eliminar un objeto utilizando: 'del carro'
"""

# Fin definicion de la clase <-----