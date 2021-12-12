#Jennie
import turtle
import time

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def easteregg(scores):
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(231, 228, 237)
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()

    pos(trtl, 0, 0) 
    trtl.write("Wow", font=("Time New Roman", 22, "bold"), align="center")
    time.sleep(1.5)
    trtl.ht()
    trtl.clear()
    return scores