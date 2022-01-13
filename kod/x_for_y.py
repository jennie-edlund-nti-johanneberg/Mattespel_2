#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle
import random
import time

#Ger slumpade nummer mellan -5 och 5
def randomNumber():
    return (int(random.randint(-3, 3)))

#Ger turtle position och färg
def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

#Körs ifall användare fick rätt
def right(score):
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

#Körs ifall användare fick fel
def wrong():
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(4)
    trtl.clear()

#Kollar om användaren har samma svar som facit
def kolla(facitk, facitm, trtl, scores):

    #Skälva skärmen läggs i variablen "sc"
    sc = turtle.Screen()
    
    #Hämtar  random siffra och tar fram det rätta svaret
    x = randomNumber()
    facity = facitk*x+facitm
    svary = None

    #Tar in användarinput (svaret)
    while svary == None:
        try:
            svary = (sc.textinput(f"Vad är y när x = {x}", 'Ditt svar (tillbaka = "return"):')) #obs här är det numera text
            if svary == "return":
                trtl.clear()
                return 
            svary = int(svary)
        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, 50, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            svary = None

    #Skriver ut användarens svar
    pen(trtl, -240, 225, "black")
    trtl.write(f"Ditt svar: y = {svary}",font=("Verdana", 12, "bold"))

    #Skriver ut rätt svar
    pen(trtl, -240, 207, "black")
    trtl.write(f"Rätt svar: y = {facity}",font=("Verdana", 12, "bold"))

    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

    #Kollar ifall användaren hade rätt
    if facity == svary:
        scores["x_for_y"] += 1
        right(scores["x_for_y"])
    else:
        scores["x_for_y"]
        wrong()

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    grid(scores)
    #sc.exitonclick() detta måste bort för att de ska funka men då kan man trycka på nej när man fyller i sina värden och få typerror som inte tas upp av undantagshantering

#Plottar själva grafen
def plotter(trtl, x_range, scores):
    trtl.penup()

    k = randomNumber()
    m = randomNumber()

    for x in x_range:
        y = (k*x + m*50)
        trtl.goto(x, y)
        trtl.color("DodgerBlue2")
        trtl.pendown()

    kolla(k, m, trtl, scores)

#Gör själva griden
def grid(scores):
    #Skapar sköldpadda + hastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)

    #x-linjerna
    for i in range(11):
        pen(trtl, -250, 250-(50*i), "lightgrey")
        trtl.fd(500)

    trtl.lt(90)

    #y-linjerna
    for i in range(11):
        pen(trtl, 250-(50*i), -250, "lightgrey")        
        trtl.fd(500)

    #Svart x-linje
    pen(trtl, 0, -250, "black")     
    trtl.fd(500)

    #Pilen till höger
    pen(trtl, 246, -8, "black") 
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Svart y-linje
    pen(trtl, -250, 0, "black")
    trtl.rt(90)
    trtl.fd(500)

    #Pilen uppåt
    pen(trtl, -6, 240, "black")
    trtl.write("^", font=("Verdana", 12, "bold"))
     
    #Skriver ut "x"
    pen(trtl, 235, 0, "black")
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    #Skriver ut "y"
    pen(trtl, 5, 235, "black")
    trtl.write("y",font=("Verdana", 12, "bold"))
    
    #Skriver ut "1"
    pen(trtl, 5, 43, "black")
    trtl.write("1",font=("Verdana", 12, "bold"))

    #Skriver ut "1"
    pen(trtl, 46, 5, "black")
    trtl.write("1",font=("Verdana", 12, "bold"))
    
    #Skriver ut "y = kx+m"
    pen(trtl, -240, -235, "black")
    trtl.write("y = kx+m",font=("Verdana", 12, "bold"))

    #Skölpaddan riktas mot höger
    trtl.setheading(0)

    #Gömmer sköldpadda
    trtl.hideturtle()

    plotter(trtl, range(-250, 250), scores)

