import turtle

# Configuración inicial
turtle.speed(2)  # Velocidad de animación
turtle.hideturtle()  # Oculta la tortuga

# Función para dibujar una estrella
def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

# Función para mover y girar la estrella al lugar del mouse
def move_and_rotate_star(x, y):
    turtle.penup()  # Levanta el lápiz para mover la tortuga sin dibujar
    turtle.goto(x, y)
    turtle.pendown()  # Baja el lápiz para dibujar

    # Gira la estrella
    for _ in range(36):  # Cambia el número de iteraciones para ajustar la rotación
        turtle.clear()  # Limpiar el dibujo anterior
        draw_star(100)
        turtle.right(10)  # Cambia el ángulo para ajustar la rotación

# Configurar la función de movimiento y rotación con el evento del mouse
turtle.onscreenclick(move_and_rotate_star)

# Dibujar una estrella inicial
draw_star(100)

# Mantener la ventana abierta
turtle.mainloop()
