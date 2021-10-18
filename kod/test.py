#Jennie (testar kod här)
from turtle import Turtle, Screen
import turtle

 # coordinate system size

def plotter(turtle, x_range):
    turtle.penup()

    for x in x_range:
        y = 2*x + 3
        ivy.goto(x, y)
        turtle.pendown()


ivy = Turtle(visible=True)
ivy.speed(0)
ivy.setheading(0)

plotter(ivy, range(-250, 250))

turtle.done()