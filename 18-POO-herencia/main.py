import clases

persona = clases.Persona()
persona.setNombre("Lautaro")
persona.setApellido("Alegria")
persona.setAltura("180cm")
persona.setEdad("27 años")

print("Persona: \n")
print(f"Mi nombre es {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

informatico = clases.Informatico()
informatico.setNombre("Cecilia")
informatico.setApellido("Cabrera")
# informatico.setAltura("162cm")
# informatico.setEdad("32 años")

print("\nInformatico: \n")
print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia) # Imprime 5 por defecto ya que es lo que esta casteado en el constructor

print("\nTecnico: \n")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Sebastian")
print(tecnico.auditarRedes)
print(tecnico.getNombre(),tecnico.getLenguajes())
# Si no uso la funcion 'super()' en el constructor de la clase 'Tecnico' el print anterior hubiera dado 
# error porque el constructor es de cada clase, si tengo un nuevo contructor en 'Tecnico' invalido el 
# constructor de 'Informatico' por lo tanto debo invocarlo con la funcion 'super()'