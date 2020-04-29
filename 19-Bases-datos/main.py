import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# # Comprobar conexion
# print(database)


# Cursor -->
cursor = database.cursor(buffered=True)

# Creo la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Comprobar si la base de datos existe -> almacena en 'cursor' todas las bases de datos existentes
cursor.execute("SHOW DATABASES")
# Imprimo las bases de datos
for bd in cursor:
    print(bd)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
);
""")

cursor.execute("SHOW TABLES")
# Como indique 'database = "master_python"' al comienzo no me trae todas las bases de datos, trabajare sobre 'master_python'
for table in cursor:
    print(table)

# Insertar un objeto
cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500);")

# Insertar varios objetos
# Creo una lista de tuplas con los objetos a insertar
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000), 
    ('Mercedes', 'Clase C', 35000)
]

# # Utilizo la funcion '.executemany(parametros, lista de tuplas)
# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
# print(cursor.rowcount, "Agregados\n")
database.commit()

# Selecciono todos los vehiculos
""" 

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("\n--- Todos mis coches ---\n")
for coche in result:
    print(coche)

"""

# Selecciono los coches con precios inferiores a 5000
"""
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000")
resultado = cursor.fetchall()

print("\n--- Vehiculos con precio menor a 5000\n")
for coche in resultado:
    print(coche[1], coche[3])
"""

# Selecciono los coches con precios inferiores a 5000 y de marca Seat
"""
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat' ")
resultado = cursor.fetchall()

print("\n--- Vehiculos con precio menor a 5000 y de marca Seat ---\n")
for coche in resultado:
    print(coche[1], coche[3])
"""
# Selecciono solo el primer elemento
"""
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)
"""

# # Borar registro
# cursor.execute("DELETE FROM vehiculos WHERE marca = 'Seat' ")
# database.commit()

# # Cuento la cantidad de columnas afectadas por el 'execute'
# print(cursor.rowcount, "Borrados")


# Actualizar registro
cursor.execute("UPDATE vehiculos SET modelo = 'Leo' WHERE marca = 'Opel' ")
database.commit()

print(cursor.rowcount, "Actualiados\n")

cursor.close()
database.close()