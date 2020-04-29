import mysql.connector

## Conexion -> Creo la conexion la cual se guardara en 'database'
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)


## Compruebo conexion
print(f"Compruebo conexion: \n {database}")
# Cursor --> buffered=True -> se utiliza cuando hay muchas ejecuciones a la base de datos para evitar errores
cursor = database.cursor(buffered=True)


## Creo la base de datos -> utilizo la sentensia 'IF NOT EXISTS' para evitar que se vuelva a crear
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")


## Comprobar si la base de datos existe -> almacena en 'cursor' todas las bases de datos existentes
cursor.execute("SHOW DATABASES")
# Imprimo las bases de datos existentes
print("\nBases de datos: \n")
for bd in cursor:
    print(bd)


## Crear tablas -> utilizo la sentensia 'IF NOT EXISTS' para evitar que se vuelva a crear
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
);
""")


# Muestro las tablas existentes
cursor.execute("SHOW TABLES")
# Como indique 'database = "master_python"' al comienzo me trae las tablas que contiene 'master_python'
# Imprimo las tablas
print("\nTablas: \n")
for table in cursor:
    print(table)


## Insertar un objeto
cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500);")


## Insertar varios objetos
# Creo una lista de tuplas con los objetos a insertar -> no ingreso el primer valor (int) ya que es autoincremental
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000), 
    ('Mercedes', 'Clase C', 35000)
]


# # Utilizo la funcion '.executemany(parametros, lista de tuplas)
# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
# 'cursor.rowcount' me indica cuantas filas fueron modificadas con el 'execute'
# Siempre debo realizar un 'commit()' a la base de datos -> esto confirma el cambio
print(cursor.rowcount, "Agregados\n")
database.commit()


## Selecciono todos los vehiculos 
# (selecciono * desde vehiculos -> selecciono todo desde la tabla vehiculos)
cursor.execute("SELECT * FROM vehiculos")
# fetchall() -> buscar todos <---> si no hay devuelve lista vacia
# fetchmany(cantidad) -> buscar hasta la cantidad ingresada <---> si no hay devuelve lista vacia
# fetchone() -> busca un solo registro (fila) <---> si no hay retorno None
result = cursor.fetchall()
print("\n--- Todos mis coches ---\n")
for coche in result:
    print(coche)


## Selecciono los coches con precios inferiores a 5000
# (selecciono * desde vehiculos donde precio sea menor o igua a 5000)
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000")
resultado = cursor.fetchall()
print("\n--- Vehiculos con precio menor a 5000\n")
# Con los indices indico que quiero imprimir -> marca y modelo
for coche in resultado:
    print(coche[1], coche[3])


## Selecciono los coches con precios inferiores a 5000 y de marca Seat
# Se utiliza el operador 'AND' cuando quiero agregar otro parametro a la busqueda
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat' ")
resultado = cursor.fetchall()
print("\n--- Vehiculos con precio menor a 5000 y de marca Seat ---\n")
for coche in resultado:
    print(coche[1], coche[3])


## Selecciono solo el primer elemento
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)


# # Borar registro
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Opel' ")
database.commit()
# Cuento la cantidad de columnas afectadas por el 'execute'
print()
print(cursor.rowcount, "borrados!")


## Actualizar registro
# (actualizar vehiculos, cambiar modelo a 'Leo' donde marca sea igual a 'Opel')
cursor.execute("UPDATE vehiculos SET modelo = 'Leo' WHERE marca = 'Opel' ")
database.commit()
# Cuento la cantidad de columnas afectadas por el 'execute'
print()
print(cursor.rowcount, "actualizados\n")

## Cuento la cantidad de filas en la tabla
cursor.execute("SELECT * FROM vehiculos")
print(cursor.rowcount, "filas activas\n")

## Siempre debo cerrar el cursor y la base de datos
cursor.close()
database.close()