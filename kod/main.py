#Jennie
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

topFrame = tk.Frame(root)
topFrame.pack()
middleFrame = tk.Frame(root)
middleFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack()

tk.Button(topFrame, text="Play", fg="blue", command=goUp).pack()

wn.mainloop()