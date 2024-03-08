import tkinter as tk

class JuegoPelota:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego de Pelota")
        self.ventana.geometry("600x400")
        self.ventana.resizable(False, False)

        self.canvas = tk.Canvas(self.ventana, bg="white", width=600, height=400)
        self.canvas.pack()

        self.velocidad_y = 0
        self.radio_pelota = 25
        self.pelota = self.canvas.create_oval(275, 275, 325, 325, fill="red")

        self.canvas.bind("<Button-1>", self.clic_mouse)
        self.aumentar_velocidad()

    def clic_mouse(self, evento):
        self.velocidad_y = -10

    def animar_pelota(self):
        self.canvas.move(self.pelota, 0, self.velocidad_y)

        pelota_pos = self.canvas.coords(self.pelota)
        if pelota_pos[3] >= 400:
            self.terminar_juego()
        elif pelota_pos[1] <= 0:
            self.velocidad_y *= -1

        self.ventana.after(30, self.animar_pelota)

    def terminar_juego(self):
        self.canvas.create_text(300, 200, text="¡Perdiste!", font=("Arial", 30), fill="red")
        self.ventana.after_cancel(self.animar_pelota)

    def aumentar_velocidad(self):
        self.velocidad_y *= 1.2
        self.ventana.after(1000, self.aumentar_velocidad)  # Aumenta la velocidad cada 15 segundos

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    juego = JuegoPelota(ventana_principal)
    juego.animar_pelota()  # Llamamos al método para comenzar la animación de la pelota
    ventana_principal.mainloop()
