import mysql.connector
import os
   

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            if(self.connection==None):
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
        except mysql.connector.Error as error:
            print("Error while connecting to database: {}".format(error))


    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
        except mysql.connector.Error as error:
            print("Error while disconnecting from database: {}".format(error))

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as error:
            print("Error while executing query: {}".format(error))



class Product:
    def __init__(self, db):
        self.db = db

    def create(self, name, price):
        try:
            query = "INSERT INTO products (name, price) VALUES (%s, %s)"
            params = (name, price)
            self.db.execute_query(query, params)
        except mysql.connector.Error as error:
            print("Error while inserting into database: {}".format(error))


    def read(self, id=None):
        try:
            if id:
                query = "SELECT * FROM products WHERE id = %s"
                params = (id,)
                result = self.db.execute_query(query, params)
            else:
                query = "SELECT * FROM products"
                result = self.db.execute_query(query)
            return result
        except mysql.connector.Error as error:
            print("Error while reading from database: {}".format(error))

    def update(self, id, name, price):
        try:
            query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
            params = (name, price, id)
            self.db.execute_query(query, params)
        except mysql.connector.Error as error:
            print("Error while updating database: {}".format(error))

    def delete(self, id):
        try:
            query = "DELETE FROM products WHERE id = %s"
            params = (id,)
            self.db.execute_query(query, params)
        except mysql.connector.Error as error:
            print("Error while deleting from database: {}".format(error))

    def show_products(self):
        try:
            result = self.read()
            for row in result:
                print(row)
        except mysql.connector.Error as error:
            print("Error while reading from database: {}".format(error))


class ProductInteraction:
    def __init__(self, db):
        self.product = Product(db)

    def create_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        self.product.create(name, price)
        print("Product created successfully!")

    def read_product(self):
        id = input("Enter product id (leave blank to read all products): ")
        if id:
            result = self.product.read(id)
        else:
            result = self.product.read()
        for row in result:
            print(row)

    def update_product(self):
        id = input("Enter product id: ")
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        self.product.update(id, name, price)
        print("Product updated successfully!")

    def delete_product(self):
        id = input("Enter product id: ")
        self.product.delete(id)
        print("Product deleted successfully!")
    
    def show_products(self):
        self.product.show_products()

def menu():
    os.system("cls")
    print("1. Create product")
    print("2. Read product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Show products")
    print("6. Exit")
    return int(input("Enter an option: "))

def main():
    db = MySQLDatabase("localhost", "root", "", "dbprueba")
    db.connect()
    product_interaction = ProductInteraction(db)
    while True:
        option = menu()
        if option == 1:
            product_interaction.create_product()
            db.connection.commit()  # Commit the transaction
            os.system("pause")
        elif option == 2:
            product_interaction.read_product()
            os.system("pause")
        elif option == 3:
            product_interaction.update_product()
            db.connection.commit()  # Commit the transaction
            os.system("pause")
        elif option == 4:
            product_interaction.delete_product()
            db.connection.commit()  # Commit the transaction
            os.system("pause")
        elif option == 5:
            product_interaction.show_products()
            os.system("pause")
        elif option == 6:
            break
        else:
            print("Invalid option")
            os.system("pause")
    db.disconnect()

if __name__ == "__main__":
    main()