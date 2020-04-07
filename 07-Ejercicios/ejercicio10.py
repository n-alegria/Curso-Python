alumnosAprobados = 0
alumnosSuspendidos = 0
contador = 1

while contador < 15:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno{contador}\"?: "))
    if nota >= 7:
        alumnosAprobados += 1
    elif nota < 7:
        alumnosSuspendidos += 1
    contador += 1

print(f"Alumnos aprobados: {alumnosAprobados}\nAlumnos Suspendidos: {alumnosSuspendidos}")