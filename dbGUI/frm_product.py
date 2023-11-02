import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from model.m_product import Product
from dao.dao_connection import DaoConnection
from dao.dao_products import DaoProduct
from tkinter import filedialog


class ProductManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        self.create_gui()
        self.initialize_db()
        self.read_all_products()

    def create_gui(self):
        # Crear un marco principal
        main_frame = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Formulario para crear y actualizar productos
        form_frame = tk.Frame(main_frame)
        main_frame.add(form_frame)

        self.label_name = tk.Label(form_frame, text="Nombre del Producto")
        self.label_price = tk.Label(form_frame, text="Precio")
        self.label_stock = tk.Label(form_frame, text="Stock")

        self.entry_name = tk.Entry(form_frame)
        self.entry_price = tk.Entry(form_frame)
        self.entry_stock = tk.Entry(form_frame)

        self.button_create = tk.Button(
            form_frame, text="Crear Producto", command=self.create_product
        )
        self.button_update = tk.Button(
            form_frame,
            text="Actualizar Producto",
            command=self.update_product,
            state=tk.DISABLED,
        )
        self.button_delete = tk.Button(
            form_frame,
            text="Eliminar Producto",
            command=self.delete_product,
            state=tk.DISABLED,
        )

        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_price.grid(row=1, column=0)
        self.entry_price.grid(row=1, column=1)
        self.label_stock.grid(row=2, column=0)
        self.entry_stock.grid(row=2, column=1)
        self.button_create.grid(row=3, column=0)
        self.button_update.grid(row=3, column=1)
        self.button_delete.grid(row=3, column=2)

        # Espacio para buscar por ID
        search_frame = tk.Frame(form_frame)
        search_frame.grid(row=4, columnspan=3)

        self.label_search = tk.Label(search_frame, text="Buscar por ID:")
        self.entry_search = tk.Entry(search_frame)
        self.button_search = tk.Button(
            search_frame, text="Buscar", command=self.search_product
        )

        self.button_export_pdf = tk.Button(
            form_frame, text="Exportar a PDF", command=self.export_to_pdf
        )
        self.button_export_pdf.grid(row=8, column=0, columnspan=3)
        

        self.label_search.grid(row=0, column=0)
        self.entry_search.grid(row=0, column=1)
        self.button_search.grid(row=0, column=2)

        # Tabla para mostrar productos
        table_frame = tk.Frame(main_frame)
        main_frame.add(table_frame)

        self.product_table = ttk.Treeview(
            table_frame, columns=("ID", "Name", "Price", "Stock")
        )
        self.product_table.heading("#1", text="ID")
        self.product_table.heading("#2", text="Nombre")
        self.product_table.heading("#3", text="Precio")
        self.product_table.heading("#4", text="Stock")

        self.product_table.bind(
            "<ButtonRelease-1>", self.on_table_click
        )  # Evento de clic en la tabla

        self.product_table.pack(fill=tk.BOTH, expand=True)

    def initialize_db(self):
        self.db = DaoConnection(
            host="localhost",
            user="root",
            password="",
            database="dbtest",
        )

    def create_product(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        stock = self.entry_stock.get()

        if not name or not price or not stock:
            messagebox.showerror("Error", "Todos los campos son requeridos.")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror(
                "Error", "El precio y el stock deben ser números válidos."
            )
            return

        product = Product(id=None, name=name, price=price, stock=stock)
        dao_product = DaoProduct(self.db)
        dao_product.create(product)

        self.clear_form()
        self.read_all_products()

    def update_product(self):
        selected_item = self.product_table.selection()
        if selected_item:
            id = self.product_table.item(selected_item, "values")[0]
            name = self.entry_name.get()
            price = self.entry_price.get()
            stock = self.entry_stock.get()

            if not name or not price or not stock:
                messagebox.showerror("Error", "Todos los campos son requeridos.")
                return

            try:
                price = float(price)
                stock = int(stock)
            except ValueError:
                messagebox.showerror(
                    "Error", "El precio y el stock deben ser números válidos."
                )
                return

            product = Product(id=id, name=name, price=price, stock=stock)
            dao_product = DaoProduct(self.db)
            dao_product.update(product)

            self.clear_form()
            self.read_all_products()

    def delete_product(self):
        selected_item = self.product_table.selection()
        if selected_item:
            id = self.product_table.item(selected_item, "values")[0]
            dao_product = DaoProduct(self.db)
            dao_product.delete(id)

            self.clear_form()
            self.read_all_products()

    def search_product(self):
        id = self.entry_search.get()
        dao_product = DaoProduct(self.db)
        product = dao_product.read(id)

        if product:
            self.product_table.delete(*self.product_table.get_children())
            self.product_table.insert(
                "", "end", values=(product[0], product[1], product[2], product[3])
            )
        else:
            messagebox.showinfo(
                "No encontrado", "El producto con el ID especificado no fue encontrado."
            )

    def on_table_click(self, event):
        selected_item = self.product_table.selection()
        if selected_item:
            self.button_update.config(state=tk.NORMAL)
            self.button_delete.config(state=tk.NORMAL)
            values = self.product_table.item(selected_item, "values")
            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_stock.delete(0, tk.END)
            self.entry_name.insert(0, values[1])
            self.entry_price.insert(0, values[2])
            self.entry_stock.insert(0, values[3])
        else:
            self.button_update.config(state=tk.DISABLED)
            self.button_delete.config(state=tk.DISABLED)

    def read_all_products(self):
        dao_product = DaoProduct(self.db)
        products = dao_product.read_all()

        self.product_table.delete(*self.product_table.get_children())

        for product in products:
            self.product_table.insert(
                "", "end", values=(product[0], product[1], product[2], product[3])
            )

    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    def export_to_pdf(self):
        # Abre un cuadro de diálogo para seleccionar la ubicación del archivo PDF
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return  # El usuario canceló la operación

        # Crear un documento PDF con ReportLab
        c = canvas.Canvas(file_path, pagesize=letter)

        # Encabezado de la tabla
        column_widths = [100, 200, 100, 100]  # Ancho de cada columna
        table_headings = ["ID", "Nombre", "Precio", "Stock"]

        y = 750  # Altura inicial de la tabla
        x = 50  # Posición inicial de x
        for heading, width in zip(table_headings, column_widths):
            c.drawString(x, y, heading)
            x += width  # Mover a la derecha para la próxima columna

        # Datos de la tabla
        data = []
        for item in self.product_table.get_children():
            values = self.product_table.item(item, "values")
            data.append(values)

        y = 720  # Altura inicial de los datos de la tabla
        for row in data:
            x = 50
            for item, width in zip(row, column_widths):
                c.drawString(x, y, str(item))
                x += width
            y -= 30

        # Guardar y cerrar el archivo PDF
        c.save()
        messagebox.showinfo(
            "Exportación Exitosa", "La tabla se exportó exitosamente a un archivo PDF."
        )