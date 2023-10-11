class Product:
    def __init__(self, name, price, stock):
        self.name = name,
        self.price = price,
        self.stock = stock
    
    def __str__(self):
        return f"Producto: {self.name}, Precio: {self.price}, Stock: {self.stock}"
    
def main():
    cafe = Product("Cafe", 1.5, 10)
    gaseosa = Product("Gaseosa", 2.5, 20)
    print(cafe, gaseosa, sep="\n")

if __name__ == "__main__":
    main()

# Path: Sesion12/ejemplo.py