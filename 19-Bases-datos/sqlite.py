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

# Cerrar conexión
conexion.close()