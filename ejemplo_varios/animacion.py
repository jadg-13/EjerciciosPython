import turtle


# Configuración inicial
turtle.speed(2)  # Velocidad de animación

# Dibuja el cuadrado
for _ in range(4):
    turtle.forward(100)  # Avanza 100 unidades
    turtle.left(90)      # Gira 90 grados a la izquierda

# Cierra la ventana al hacer clic en ella
turtle.exitonclick()