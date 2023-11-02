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
        except mysql.connector.Error as error:
            print("Error Conex", error)
        return self.cursor
    
    def disconnect(self):
        try:
            self.cursor.close()
            self.connection.close() 
        except mysql.connector.Error as error:
            print(error)
        return self.cursor
    
    def execute(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as error:
            print(error)
        return self.cursor  
