import os
from PIL import Image
from tkinter import Tk, Label, Button, filedialog, Entry

input_folder_path = ""
output_folder_path = ""


def choose_input_folder():
    global input_folder_path
    input_folder_path = filedialog.askdirectory(
        title="Seleccione la carpeta de entrada"
    )
    if input_folder_path:
        input_folder_label.config(text="Carpeta de entrada seleccionada")


def choose_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory(
        title="Seleccione la carpeta de destino"
    )
    if output_folder_path:
        output_folder_label.config(text="Carpeta de destino seleccionada")


def resize_image(input_path, output_path, target_width, target_height):
    img = Image.open(input_path)
    img_resized = img.resize((target_width, target_height))
    img_resized.save(output_path)


def process_images():
    global input_folder_path, output_folder_path

    if input_folder_path and output_folder_path:
        target_width = int(width_entry.get())
        target_height = int(height_entry.get())

        for file in os.listdir(input_folder_path):
            if file.lower().endswith(".png"):
                file_path = os.path.join(input_folder_path, file)
                new_file_path = os.path.join(
                    output_folder_path, os.path.splitext(file)[0] + ".png"
                )
                resize_image(file_path, new_file_path, target_width, target_height)

        message_label.config(text="¡Procesamiento completado!")


# GUI setup
window = Tk()
window.title("Redimensionador de Imágenes")
window.geometry("400x300")

input_folder_label = Label(window, text="Seleccione la carpeta de entrada")
input_folder_label.pack(pady=10)
input_folder_button = Button(
    window, text="Seleccione la carpeta de entrada", command=choose_input_folder
)
input_folder_button.pack()

output_folder_label = Label(window, text="Seleccione la carpeta de destino")
output_folder_label.pack(pady=10)
output_folder_button = Button(
    window, text="Seleccione la carpeta de destino", command=choose_output_folder
)
output_folder_button.pack()

width_label = Label(window, text="Ancho objetivo:")
width_label.pack()
width_entry = Entry(window)
width_entry.pack()

height_label = Label(window, text="Alto objetivo:")
height_label.pack()
height_entry = Entry(window)
height_entry.pack()

process_button = Button(window, text="Procesar imágenes", command=process_images)
process_button.pack(pady=10)

message_label = Label(window, text="")
message_label.pack()

window.mainloop()
