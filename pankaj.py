from turtle import*
from colorsys import hsv_to_rgb
speed(0)
bgcolor ("black")
h=0
for i in range (240):
    h +=0.0015
    r,g,b =hsv_to_rgb(h, 1, 1)
    color (r,g,b)
    penup()
    goto(0,0)
    pendown()
    forward(i)
    right(70)
    circle(100,500)
    right(10)
    left(70)
       
 #move the done()
