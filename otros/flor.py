from turtle import *
import colorsys

tracer(10)
h = 0.3
pensize(2)
bgcolor('green')
for i in range(180):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h+= 0.004
    fd(20)
    circle(i-190, 100)
    rt(80)
    circle(1-190, 100)
    for j in range(5):
        rt(20)
        lt(20)
    lt(50)

hideturtle()
done