import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        # Cifrar contraseña
        # Creo un objeto del tipo 'hashlib', luego debo actualizarlo y pasarle una codificacion a 'byte'
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        # Se almacena en forma hexadecimal
        usuario = (self.nombre, self. apellido, self.email, cifrado.hexdigest(), fecha)
        # El email es unico, es sensible a errores, por eso se introduce dentro del 'try'
        try:
        # Paso como parametros al 'execute' los datos almacenados en las variables
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        # Consulta para comprobar si existe usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        # Cifrar contraseña
        # Creo un objeto del tipo 'hashlib', luego debo actualizarlo y pasarle una codificacion a 'byte'
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))
        # Datos para consulta
        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql, usuario)
        # Resultado consulta
        resultado = cursor.fetchone()
        return resultado
