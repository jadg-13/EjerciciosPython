import mysql.connector
from os import system

# Datos de la conexion
host = "mysql-5707.dinaserver.com"
port = 3306
user = "mouredev_read"
password = "mouredev_pass"
database = "moure_test"

# Conectar con la base de datos
connection = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# Cursor para ejecutar la consulta
cursor = connection.cursor()

# Ejecutar la consulta
query = "SELECT id as Código, name as Nombre, difficulty as Dificultad, date as Fecha FROM challenges"
cursor.execute(query)

system("cls")
column_names = [desc[0] for desc in cursor.description]
print(f"{column_names[0].center(8).upper()} | {column_names[1].center(40).upper()} | {column_names[2].center(10).upper()} | {column_names[3].center(10).upper()}")

# Imprimir el resultado
for row in cursor:
    print(f"{row[0]:>8} | {row[1]:<40} | {row[2]: <10} | {row[3]}")

# Cerrar el cursor y la conexión
cursor.close()
connection.close()
