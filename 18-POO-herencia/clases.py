# Herencia: posibilidad de compartir atributos y metodos entre clases. Y que diferentes clases hereden de otras.

class Persona:
# --> Atributos
    """
    nombre
    apellido
    altura
    edad
    """
# <-- Fin Atributos

# --> Setter - Getter
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.altura = edad
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

# <-- Fin Setter - Getter

# --> Metodos
    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"
# <-- Fin Metodos

# --> Constructor

# <-- Fin Constructor

# <---------------------------------

# Para heredar debo introducir dentro de los parentesis la clase de la cual voy a heredar
class Informatico(Persona):
    # --> Atributos
    """
    lenguajes
    experiencia
    """
    # <-- Fin Atributos

    # --> Constructor
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavasCript, PHP"
        self.experiencia = 5
    # <-- Fin Constructor

    # --> Metodos
    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador"
    # <-- Fin Metodos

# <---------------------------------

class TecnicoRedes(Informatico):

    def __init__(self):
        # Con 'super().__init__' indico que herede el constructor de la clase que hereda
        super().__init__()
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"