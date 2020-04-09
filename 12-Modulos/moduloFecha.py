# Modulo Fechas
import datetime

print(datetime.date.today())

# Almaceno la fecha completa y hora actual en la variable
fecha_completa = datetime.datetime.now()
print(fecha_completa)

# Puedo acceder a los datos individuales
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

# Personalizo la fecha %d-dia, %m-mes, %Y-anio
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())