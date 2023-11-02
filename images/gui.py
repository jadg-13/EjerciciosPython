import os
from tkinter import (
    Tk,
    Label,
    Button,
    filedialog,
    OptionMenu,
    StringVar,
    Entry,
    colorchooser,
)
from PIL import Image, ImageOps

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


def choose_background_color():
    color = colorchooser.askcolor(title="Seleccione un color")
    if color:
        background_color_entry.delete(0, "end")
        background_color_entry.insert(0, ",".join(map(str, color[0])))


def test():
    print(input_folder_path)


def process_images():
    global input_folder_path, output_folder_path

    if input_folder_path and output_folder_path:
        os.makedirs(output_folder_path, exist_ok=True)

        file_format = (
            file_format_var_input.get()
        )  # Obtiene el formato de salida seleccionado
        background_color = tuple(
            map(int, background_color_entry.get().split(","))
        )  # Obtiene el color de fondo
        target_width = int(width_entry.get())  # Obtiene el ancho objetivo
        target_height = int(height_entry.get())  # Obtiene el alto objetivo
        padding = int(padding_entry.get())  # Obtiene el valor de padding

        for root, dirs, files in os.walk(input_folder_path):
            for file in files:
                if file.lower().endswith(".png"):
                    file_path = os.path.join(root, file)
                    img = Image.open(file_path)

                    # Convierte la imagen PNG a modo RGBA
                    img = img.convert("RGBA")

                    # Crea una nueva imagen con fondo blanco
                    background = Image.new("RGBA", img.size, background_color)

                    # Combina la imagen original con el fondo blanco
                    new_img = Image.alpha_composite(background, img)

                    # Calcula las dimensiones para aplicar el padding
                    target_size = (target_width, target_height)
                    padding = padding

                    # Aplica el padding
                    img_resized = ImageOps.pad(
                        new_img,
                        target_size,
                        color=background_color,
                        centering=(0.5, 0.5),
                    )
                    img_resized = ImageOps.expand(
                        img_resized, padding, fill=background_color
                    )

                    # Guarda la imagen como png
                    new_file_path = os.path.join(
                        output_folder_path, os.path.splitext(file)[0] + ".png"
                    )
                    img_resized.convert("RGB").save(new_file_path, "JPEG")

        message_label.config(text="¡Processing completed!")


# Crear la ventana principal
window = Tk()
window.title("Taopic")
window.geometry("400x600")

# Etiqueta y botón para seleccionar la carpeta de entrada
input_folder_label = Label(window, text="Select the input folder")
input_folder_label.pack(pady=10)
input_folder_button = Button(
    window, text="Select the input folder", command=choose_input_folder
)
input_folder_button.pack()

# Etiqueta y botón para seleccionar la carpeta de destino
output_folder_label = Label(window, text="Select the output folder")
output_folder_label.pack(pady=10)
output_folder_button = Button(
    window, text="Select the output folder", command=choose_output_folder
)
output_folder_button.pack()

# Etiqueta de instrucciones
instruction_label = Label(window, text="Input image format")
instruction_label.pack(pady=10)

# Etiqueta y menú desplegable para las imagenes de entrada
file_input_images_format = Label(window, text="input image format:")
file_input_images_format.pack()
file_input_formats_select = [".png"]
file_format_var_input = StringVar(window)
file_format_var_input.set(file_input_formats_select[0])  # Valor predeterminado
file_format_dropdown_input = OptionMenu(
    window, file_format_var_input, *file_input_formats_select
)
file_format_dropdown_input.pack()

# Etiqueta y menú desplegable para las imagenes de salida
file_input_images_format = Label(window, text="Output image format")
file_input_images_format.pack()
file_input_formats_select = [".png"]
file_format_var_input = StringVar(window)
file_format_var_input.set(file_input_formats_select[0])  # Valor predeterminado
file_format_dropdown_input = OptionMenu(
    window, file_format_var_input, *file_input_formats_select
)
file_format_dropdown_input.pack()

# Etiqueta, campo de entrada y botón para el color de fondo
background_color_label = Label(window, text="Background color")
background_color_label.pack()

background_color_entry = Entry(window)
background_color_entry.pack()

choose_color_button = Button(window, text="Select", command=choose_background_color)
choose_color_button.pack()

# Etiqueta y campo de entrada para el ancho objetivo
width_label = Label(window, text="Objective width:")
width_label.pack()
width_entry = Entry(window)
width_entry.pack()

# Etiqueta y campo de entrada para el alto objetivo
height_label = Label(window, text="Ojective height:")
height_label.pack()
height_entry = Entry(window)
height_entry.pack()

# Etiqueta y campo de entrada para el padding
padding_label = Label(window, text="Padding:")
padding_label.pack()
padding_entry = Entry(window)
padding_entry.pack()

# Botón para iniciar el procesamiento
process_button = Button(window, text="Process images", command=process_images)
process_button.pack(pady=10)

# Etiqueta para mostrar el mensaje de finalización
message_label = Label(window, text="")
message_label.pack()

# Ejecutar el bucle principal de la interfaz gráfica
window.mainloop()
