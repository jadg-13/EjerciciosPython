import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None

class TablasDeBaseDeDatos:
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrar_tablas(self):
        if self.conexion.conexion:
            cursor = self.conexion.conexion.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            cursor.close()
            if tables:
                print("Tablas en la base de datos:")
                for table in tables:
                    print(table[0])
                    nombre_tabla = table[0]
                    tsql = "select * from " + nombre_tabla
                    cursor = self.conexion.conexion.cursor()
                    cursor.execute(tsql)
                    registros = cursor.fetchall()
                    print("Registros en la tabla " + nombre_tabla)
                    for registro in registros:
                        print(registro)
                    cursor.close()
                    
            else:
                print("No se encontraron tablas en la base de datos.")
        else:
            print("No hay una conexión de base de datos activa.")


print("Conexión a la base de datos")
print("-"*30)
host = input("Host: ")
user = input("User: ")
password = input("Password: ")
database = input("Database: ")
conexion = Conexion(host, user, password, database)
conexion.conectar()
print("Conexión exitosa")

conexion = Conexion(host, user, password, database)
conexion.conectar()

if conexion.conexion:
    tablas = TablasDeBaseDeDatos(conexion)
    tablas.mostrar_tablas()


conexion.desconectar()
print("Desconexión exitosa")
print("-"*30)
print("Fin del programa")
