import tkinter as tk

import requests
from frm_product import ProductManagementApp
from tkinter import messagebox
from PIL import Image, ImageTk


class MainForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Principal")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Maximizar la ventana al inicio
        self.root.wm_state("zoomed")

        self.create_gui()

    def create_gui(self):
        # Etiqueta de título
        title_label = tk.Label(
            self.root,
            text="CRUD para el registro de Productos",
            font=("Helvetica", 16),
        )
        title_label.pack()

        # imagen logo de python de internet
        image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png"
        image = Image.open(requests.get(image_url, stream=True).raw)
        photo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(self.root, image=photo)
        logo_label.image = photo
        logo_label.pack()

        # Botón para abrir la gestión de productos
        button_open_product_management = tk.Button(
            self.root,
            text="Abrir Gestión de Productos",
            command=self.open_product_management,
        )
        button_open_product_management.pack()

        # Etiqueta de dedicatoria
        dedicatoria_label = tk.Label(
            self.root,
            text="""
            Dedicado a mis estudiantes: 
            
            - Carlos Talavera, 
            - Enrique Taleno,
            - Diego Mora
            
            Gracias por este Workshop!
            
            Éxito en sus proyectos!
            
            - Ing José A. Durán G.
            """,
            font=("Helvetica", 12),
        )
        dedicatoria_label.pack()

    def open_product_management(self):
        root_product_management = tk.Toplevel()
        app = ProductManagementApp(root_product_management)

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    main_form = MainForm(root)
    root.mainloop()

"""
Nota:

Para que funcione el exportar a PDF deben instalar el paquete
reportlab con el siguiente comando:

pip install reportlab

"""