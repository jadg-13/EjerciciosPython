class DaoProduct:
    def __init__(self, db):
        self.db = db

    def create(self, product):
        try:
            query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
            values = (product.name, product.price, product.stock)
            self.db.connect()
            self.db.execute(query, values)
            self.db.disconnect()
        except Exception as error:
            print(error)
    
    def read(self, id):
        try:
            query = "SELECT * FROM products WHERE id = %s"
            values = (id,)
            self.db.connect()
            self.db.execute(query, values)
            product = self.db.cursor.fetchone()
            self.db.disconnect()
            return product
        except Exception as error:
            print(error)
    
    def read_all(self):
        try:
            query = "SELECT * FROM products"
            self.db.connect()
            self.db.execute(query, None)
            products = self.db.cursor.fetchall()
            self.db.disconnect()
            return products
        except Exception as error:
            print("Error", error)
    
    def update(self, product):
        try:
            query = "UPDATE products SET name = %s, price = %s, stock = %s WHERE id = %s"
            values = (product.name, product.price, product.stock, product.id)
            self.db.connect()
            self.db.execute(query, values)
            self.db.disconnect()
        except Exception as error:
            print(error)
    
    def delete(self, id):
        try:
            query = "DELETE FROM products WHERE id = %s"
            values = (id,)
            self.db.connect()
            self.db.execute(query, values)
            self.db.disconnect()
        except Exception as error:
            print(error)
    
    def delete_all(self):
        try:
            query = "DELETE FROM products"
            self.db.connect()
            self.db.execute(query, None)
            self.db.disconnect()
        except Exception as error:
            print(error)
    
    def count(self):
        try:
            query = "SELECT COUNT(*) FROM products"
            self.db.connect()
            self.db.execute(query, None)
            count = self.db.cursor.fetchone()
            self.db.disconnect()
            return count
        except Exception as error:
            print(error)
    
    def exists(self, id):
        try:
            query = "SELECT COUNT(*) FROM products WHERE id = %s"
            values = (id,)
            self.db.connect()
            self.db.execute(query, values)
            count = self.db.cursor.fetchone()
            self.db.disconnect()
            return count
        except Exception as error:
            print(error)



