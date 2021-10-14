#Jennie
import math
import time
import random
import turtle

def kordinater():
    return (int(random.randint(-5, 5)))

def kolla(facitx, facity, trtl, score):
    sc = turtle.Screen()
    #sc.setup(600, 600)
    svarx = (sc.numinput("Vad är x-kordinaten", "Ditt svar:"))
    svary = (sc.numinput("Vad är y-kordinaten", "Ditt svar:"))

    if facitx == svarx and facity == svary:
        score += 1
        newScore = right(score)
        #print("rätt")
    else:
        wrong()
        newScore = score
        #print("nej")
    trtl.clear()
    padda(newScore)

def right(score):
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

def wrong():
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()

def padda(score):
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
    trtl.sety(y*50-7)
    trtl.color("red", "red")
    trtl.begin_fill()
    trtl.pd()
    trtl.circle(7)
    trtl.end_fill()

    trtl.hideturtle()

    kolla(x, y, trtl, score)

def omgång():
    print(" ")

padda(0)