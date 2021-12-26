#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
import random
import turtle

#Ger kordinat mellan -5 och 5 som inte är 0
def rand_cord():
    exclude=[0]
    randInt = random.randint(-4,4)
    return rand_cord() if randInt in exclude else randInt 

#ger facit
def facitet(x, y):
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
       return 3
    else:
        return 4

#Ger en position och färg till trtl
def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

#Rätt svar
def right(score):
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

#Fel svar
def wrong():
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(4)
    trtl.clear()


#Kollar om användaren har samma svar som facit
def check(facit_kvad, trtl, scores):

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (svaren)
    while user_guess == None:
        try:
            user_guess = (sc.textinput("Vilken kvadrant", "Ditt svar (return = tillbaka):")) #obs här är det numera text
            if user_guess == "return":
                trtl.clear()
                return
            user_guess = int(user_guess)
        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, 50, 100, "grey")
            trtl_2.write("Testa igen", font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            user_guess = None
        

    #Skriver ut användarens svar
    pen(trtl, -240, 225, "black")
    trtl.write(f"Ditt svar: ({int(user_guess)})",font=("Verdana", 12, "bold"))

    #Skriver ut rätt svar
    pen(trtl, -240, 207, "black")
    trtl.write(f"Rätt svar: ({facit_kvad})",font=("Verdana", 12, "bold"))

    #Väntar 2 sekunder
    trtl.hideturtle()
    time.sleep(2)

    #Kollar ifall användaren hade rätt
    if user_guess==facit_kvad:
        scores["kvadrant"] += 1
        right(scores["kvadrant"])
    else:
        scores["kvadrant"] = 0
        wrong()

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    game(scores)

#Gör kordinatsystemet och kör allt 
def game(scores):
    #Skapar trtl + maxhastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)

    #ritat ut x-linjerna
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

    #Tar in slumpmässigt x och y
    x = rand_cord()
    y = rand_cord()

    #Målar ut kordinaten i rött
    trtl.pu()
    trtl.setx(x*50)
    trtl.sety(y*50-7)
    trtl.color("red", "red")
    trtl.begin_fill()
    trtl.pd()
    trtl.circle(7)
    trtl.end_fill()

    #Gömmer sköldpadda
    trtl.hideturtle()

    #Klar med sköldpadda
    facit=facitet(x, y)
    check(facit, trtl, scores)