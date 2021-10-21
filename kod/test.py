#Jennie (testar kod här)
from turtle import Turtle, Screen
import turtle
from tkinter import *

import tkinter as tk
from turtle import RawTurtle, TurtleScreen

def goUp():
    bob.sety(bob.ycor() + 5)

def goDown():
    bob.sety(bob.ycor() - 5)

def goRight():
    bob.setx(bob.xcor() + 5)

def goLeft():
    bob.setx(bob.xcor() - 5)

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

wn = TurtleScreen(canvas)

bob = RawTurtle(wn, shape="turtle")
bob.penup()

topFrame = tk.Frame(root)
topFrame.pack()
middleFrame = tk.Frame(root)
middleFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack()

tk.Button(topFrame, text="Up", fg="red", command=goUp).pack()
tk.Button(middleFrame, text="Left", fg="red", command=goLeft).pack(side=tk.LEFT)
tk.Button(middleFrame, text="Right", fg="red", command=goRight).pack(side=tk.RIGHT)
tk.Button(bottomFrame, text="Down", fg="red", command=goDown).pack()

wn.mainloop()

# global x
# global y 

# x = 1
# y = 1
# i = 0

# root = Tk()

# wn = turtle.Screen()
# bob = turtle.Turtle()
# bob.up()

# def goUp():
#     global x, y
#     y=y+5
#     bob.goto(x,y)
# def goDown():
#     global x, y
#     y=y-5
#     bob.goto(x,y)
# def goRight():
#     global x, y
#     x=x+5
#     bob.goto(x,y)
# def goLeft():
#     global x, y
#     x=x-5
#     bob.goto(x,y)

# topFrame = Frame(root)
# topFrame.pack()
# middleFrame = Frame(root)
# middleFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack()

# button1 = Button(topFrame, text = "Up", fg="red", command=goUp)
# button2 = Button(middleFrame, text = "Left", fg="red", command=goLeft)
# button3 = Button(middleFrame, text = "Right", fg="red", command=goRight)
# button4 = Button(bottomFrame, text = "Down", fg="red", command=goDown)

# button1.pack()
# button2.pack(side=LEFT)
# button3.pack(side=RIGHT)
# button4.pack()
# root.mainloop()