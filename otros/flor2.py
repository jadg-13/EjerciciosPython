import turtle
import colorsys as cs
turtle.setup(800, 800)
turtle.speed(0)
turtle.width(2)
turtle.bgcolor("black")
for j in range(25):
    for i in range(25):
        turtle.color(cs.hsv_to_rgb(i/15, j/25, 1))
        turtle.right(90)
        turtle.circle(200-j*4, 90)
        turtle.left(90)
        turtle.circle(200-j*4, 90)
        turtle.right(180)
        turtle.circle(50, 24)
turtle.hideturtle
turtle.done