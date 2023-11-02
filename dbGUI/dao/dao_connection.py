import mysql.connector

class DaoConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
            return None

    
    def disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
        except mysql.connector.Error as error:
            print("Error al desconectar de la base de datos:", error)
        finally:
            self.cursor = None
            self.connection = None

    
    def execute(self, query, values):
        try:
            self.cursor.execute(query, values)
            # Verificar si la consulta es de lectura (SELECT)
            if query.strip().lower().startswith('select'):
                return self.cursor              
            self.connection.commit()
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta-> ", error)
        return self.cursor

