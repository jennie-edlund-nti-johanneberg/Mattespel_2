#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle
import random
import time

#Ger slumpade nummer mellan -10 och 10
def randomNumber():
    return (int(random.randint(-15, 15)))

#Ger slumpade nummer mellan -5 och 5
def randomNumber_nr2():
    return (int(random.randint(0, 3)))

#Ger turtle position och färg
def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

#Körs ifall användare fick rätt
def right(score):
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    pen(trtl, -15, 100, "black")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

#Körs ifall användare fick fel
def wrong():
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    pen(trtl, -15, 100, "black")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(4)
    trtl.clear()

#Kollar om användaren har samma svar som facit
def kolla(facity, trtl, scores):
    #Skälva skärmen läggs i variablen "sc"
    sc = turtle.Screen()
    svary = None

    #Tar in användarinput (svaren)
    while svary == None:
        try:
            svary = (sc.textinput("Vad är y?", "Ditt svar (return = tillbaka):"))
            if svary == "return":
                trtl.clear()
                return 
            svary = float(svary)
        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, -85, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            svary = None

    pen(trtl, -240, 225, "black")
    trtl.write(f"Ditt svar: y = {int(svary)}",font=("Verdana", 12, "bold"))

    pen(trtl, -240, 207, "black")
    trtl.write(f"Rätt svar: y = {facity}",font=("Verdana", 12, "bold"))

    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

    #Kollar ifall användaren hade rätt
    if facity == svary:
        scores["potensiell"] += 1
        right(scores["potensiell"])
    else:
        scores["potensiell"]= 0
        wrong()
       

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    grid(scores)
    #sc.exitonclick()

def fyrkant(trtl):
    pen(trtl, -110, 60, "red")
    trtl.fd(210)
    trtl.rt(90)
    trtl.fd(80)
    trtl.rt(90)
    trtl.fd(210)
    trtl.rt(90)
    trtl.fd(80)

#Gör själva ekvationen
def ekvation_y(trtl, scores):
    trtl.penup()

    c = randomNumber()
    a = randomNumber_nr2()
    x = randomNumber()
    y = c*x**a

    pen(trtl, -90, 30, "black")
    trtl.write(f"y = {c} * (x)^{a}",font=("Verdana", 12, "bold"))

    pen(trtl, -90, 0, "black")
    trtl.write(f"Vad är y om x = {x}",font=("Verdana", 12, "bold"))

    fyrkant(trtl)

    kolla(y, trtl, scores)

#Gör själva griden
def grid(scores):
    #Skapar sköldpadda + hastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)
    
    #Skriver ut "y = C*a^x"
    pen(trtl, -50, -50, "black")
    trtl.write("y = Ca^x",font=("Verdana", 12, "bold"))

    #Gömmer sköldpadda
    trtl.hideturtle()

    ekvation_y(trtl, scores)