import math
import random
import turtle

def kordinater():
    return (int(random.randint(-5, 5)))

def kolla(facitx, facity):
    sc = turtle.Screen()
    #sc.setup(600, 600)
    svarx = (sc.numinput("Vad är x-kordinaten", "Ditt svar:"))
    svary = (sc.numinput("Vad är y-kordinaten", "Ditt svar:"))

    if facitx == svarx and facity == svary:
        print("rätt")
    else:
        print("nej")

def padda():
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.color("lightgrey")
    # trtl.pu()
    # trtl.setx(-250)
    # trtl.sety(250)
    # trtl.pd()

    for i in range(11):
        trtl.pu()
        trtl.setx(-250)
        trtl.sety(250-(50*i))
        trtl.pd() 
        trtl.fd(500)

    trtl.lt(90)

    for i in range(11):
        trtl.pu()
        trtl.setx(250-(50*i))
        trtl.sety(-250)
        trtl.pd() 
        trtl.fd(500)

    trtl.pu()
    trtl.setx(0)
    trtl.sety(-250)
    trtl.color("black")
    trtl.pd() 
    trtl.fd(500)

    trtl.pu()
    trtl.setx(-250)
    trtl.sety(0)
    trtl.rt(90)
    trtl.pd() 
    trtl.fd(500)

    x = kordinater()
    y = kordinater()

    trtl.pu()
    trtl.setx(x*50)
    trtl.sety(y*50-5)
    trtl.color("red", "red")
    trtl.begin_fill()
    trtl.pd()
    trtl.circle(5)
    trtl.end_fill()

    trtl.hideturtle()

    kolla(x, y)
    turtle.done()

def omgång():
    print(" ")

padda()
