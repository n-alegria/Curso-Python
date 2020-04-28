import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor -> permite ejecutar consultas
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"titulo VARCHAR(225), " +
"descripcion TEXT, " +
"precio int(255)" +
")")

# Guardar cambios - commit
conexion.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()

# Listar datos
# cursor.execute("SELECT * FROM productos")
# productos = cursor.fetchall()
# print(productos)

# Cerrar conexión
conexion.close()