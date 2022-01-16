#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle
import time
import explain
scores = {"koordinater":0,"kvadrant":0, "givengraf":0, "x_for_y":0, "potensiell":0, "funktion_tabell":0, "expo": 0}

def minigames(user_choise):
    global scores
    if user_choise==0:
        explain.koordinat_explain()
        import kordinater
        kordinater.padda(scores)
    elif user_choise==1:
        explain.kvadrant_explain()
        import kvadrant
        kvadrant.game(scores)
    elif user_choise==2:  
        explain.x_for_y_explain()
        import x_for_y
        x_for_y.grid(scores)
    elif user_choise==3:
        explain.givenGraf_explain()
        import givenGraf
        givenGraf.grid(scores) 
    elif user_choise==4:
        explain.funktio_tabell_explain()
        import funktio_tabell
        funktio_tabell.game(scores)
    elif user_choise==5:
        explain.potensiell_explain()
        import potensiell
        potensiell.grid(scores)
    elif user_choise==6:
        explain.expo_explain()
        import expo
        expo.grid(scores)
    elif user_choise==7:
        import easteregg
        easteregg.easteregg(scores)
    else:
        #run funny program
        print(user_choise)

def flytt(trtl, length):
    trtl.pu()
    trtl.fd(length)
    trtl.pd

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def game_hub():
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(231, 228, 237)
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    trtl.pu()

    pos(trtl, -320, 230) 
    trtl.write("Välkommen till mattespelet!", font=("Time New Roman", 22, "bold"), align="left")
    
    pos(trtl, -320, 180)
    trtl.write("Välj ett minispel genom att skriva 0-6", font=("Time New Roman", 15, "normal"), align="left")

    pos(trtl, -300, 140) 

    minispel=["Bestämma x- och y-kordinat av en punkt","Bestämma vilken kvadrant en punkt befinner sig i","Bestämma y-värdet på specifika x-värden för räta linjer ","Räta linjens ekvation (y=kx+m)","Värdetabell för räta linjer ","Potensfunktioner","Exponentialfunktioner"]
    temp = 0

    for n in (minispel):
        trtl.write(str(minispel.index(n)) + " - " + n, font=("Time New Roman", 15, "normal"), align="left")

        temp += 1
        x_kord = (140 - temp*30)
        pos(trtl, -300, x_kord)

    pos(trtl, -320, -90)
    trtl.write("Du tar dig tillbaka hit genom att skriva return i rutan ", font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -120)
    trtl.write("som kommer upp när du är i minispelen!!!!", font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -160)
    trtl.write('Skriv "stop" för att avsluta HELA spelet', font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -200)
    trtl.write("Lycka till!", font=("Time New Roman", 15, "normal"), align="left")

    pos(trtl, 380, 200)
    trtl.write("POÄNG:", font=("Time New Roman", 15, "bold"), align="left")

    scores_uppdelad = [scores["koordinater"],scores["kvadrant"],scores["x_for_y"],scores["givengraf"],scores["funktion_tabell"],scores["potensiell"],scores["expo"]]
    pos(trtl, 380, 175)
    temp = 0

    for n in (scores_uppdelad):
        trtl.write(" → " + str(n), font=("Time New Roman", 12, "normal"), align="left")

        temp += 1
        y_kord = (175 - temp*30)
        pos(trtl, 380, y_kord)

    #window.exitonclick()

    trtl.ht()
    # window.exitonclick()

    time.sleep(1)

    #ta in user input oc se till att de är en intiger mellan 0 0ch (6+1) hehe annars få dem att skriva in igen
    sc = turtle.Screen()
    user_input = None

    #Tar in användarinput (svaret)
    while user_input == None:
        try:
            user_input = (sc.textinput("Vart vill du 0-7","Ditt val:"))
            if user_input == "stop":
                window.bye()
            user_input = int(user_input)
        except (TypeError, OverflowError, ValueError):
            time.sleep(1)
            continue
        break


    turtle.clearscreen()
    
    minigames(user_input)
    trtl.clear()
    time.sleep(0.5)
    game_hub()

game_hub()

#undantagshantering så man inte kan trycka cancle

#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf