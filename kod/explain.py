#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle
import time


def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def koordinat_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att du skriver in y-koordinaten och x-koordinaten till en punkt", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("x-koordinaten kan läsas genom att titta vart punkten ligger på x-axeln. Där x-axeln är den horisontella linjen", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 100)
    trtl.write("y-koordinaten hittas på samma sätt men du tittar på y-axeln. Den lodräta linjen.", font=('arial',15,'normal'), align='left')

    pos(trtl, 0, 0)
    trtl.pd()
    trtl.rt(0)
    trtl.fd(200)

    pos(trtl, -100, -100)
    trtl.pd()
    trtl.rt(-90)
    trtl.fd(200)

    #Pilen uppåt
    pos(trtl, -5, -5)
    trtl.write("^", font=("Verdana", 12, "bold"))

    #Pilen till höger
    pos(trtl, 100, -107)
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Skriver ut "x"
    pos(trtl, 100, -96)
    trtl.write("x",font=("Verdana", 12, "bold"))

    #Skriver ut "y"
    pos(trtl, 10, -5)
    trtl.write("y",font=("Verdana", 12, "bold"))

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) 
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def kvadrant_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att du skriver in vilken kvadrant en punkt befinner sig i", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Det finns fyra stycken kvadranter den första är längst uppe till höger.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540,100)
    trtl.write("Kolla bilden nedan:", font=('arial',15,'normal'), align='left')

    pos(trtl, 0, 0)
    trtl.pd()
    trtl.rt(0)
    trtl.fd(200)


    pos(trtl, -100, -100)
    trtl.pd()
    trtl.rt(-90)
    trtl.fd(200)

    #Pilen uppåt
    pos(trtl, -5, -5)
    trtl.write("^", font=("Verdana", 12, "bold"))

    #Pilen till höger
    pos(trtl, 100, -107)
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Skriver ut "x"
    pos(trtl, 100, -96)
    trtl.write("x",font=("Verdana", 12, "bold"))

    #Skriver ut "y"
    pos(trtl, 10, -5)
    trtl.write("y",font=("Verdana", 12, "bold"))

    #Skriver ut "1"
    pos(trtl, 50, -50)
    trtl.write("1",font=("Verdana", 12, "bold"))

    #Skriver ut "2"
    pos(trtl, -50, -50)
    trtl.write("2",font=("Verdana", 12, "bold"))

    #Skriver ut "3"
    pos(trtl, -50, -150)
    trtl.write("3",font=("Verdana", 12, "bold"))

    #Skriver ut "4"
    pos(trtl, 50, -150)
    trtl.write("4",font=("Verdana", 12, "bold"))

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def givenGraf_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att bestämma en rät linjes k-värde och m-värde (y = kx+m)", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Linjen ritas ut.", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("K-värdet kan räknas ut genom att ta ∆y/∆x = k. (Triangeln står för delta, differensen av värdet).", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Välj två koordinater på linjen. Ta sedan y-värdet på den ena koordinaten och subtrahera med den andra koordinatens y-värde.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Dividera sedan värdet du får med differensen mellan första och andra koordinatens x-värde.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Ett exempel med koordinaterna p1=(2,2) och p2=(4,8). Detta ger oss ∆y/∆x = (p2y-p1y)/(p2x-p1x) = (8-2)/(4-2) = 3. k = 3.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -100)
    trtl.write("(Tips är att ta punkten med större värden på x och y först).", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -150)
    trtl.write("M-värdet är y-värdet när funktionen går genom y-axeln, när x = 0. Eftersom y=k*0+m => y = m", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -200)
    trtl.write("(Ibland kommer det inte synas när funktionen går genom y-axeln utan man får ränka på det)", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -250)
    trtl.write("Tycker du detta är svårt kan det vara bra att träna på koordinater mer!", font=('arial',15,'italic'), align='left')

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def expo_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att du ska räkna ut vad y-värdet på en exponentialfunktion", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Exponensialfunktioner skrivs ut y = C*a^x och du kommer att få ut C-, a- och x-värdet.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Här kan miniräknare vara ett bra hjälpmedel!", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Exemple kan vara y = 3*1^x där x = 2. Detta ger oss y = 3*1^2 = 3.", font=('arial',15,'normal'), align='left')

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def potensiell_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att du ska räkna ut y-värdet på en potensfunktion", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Potensfunktioner skrivs ut y = C*x^a och du kommer att få ut C-, a- och x-värdet.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Här kan miniräknare vara ett bra hjälpmedel!", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Exempel kan vara y = 3*x^4 där x = 2. Detta ger oss y = 3*2^4 = 48.", font=('arial',15,'normal'), align='left')

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def x_for_y_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du ska bestämma vad y-värdet är på räta linjens ekvation", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Räta linjens ekvation skrivs ut y = kx+m och en sådan funktion kommer att ritas ut.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Du kommer sedan att få ut ett x-värde och du får då med hjälp av grafen läsa av y-värdet där x-värdet är.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Ibland kan linjen vara utanför grafen och då är det upp till dig att räkna ut vad y-värdet är.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Om du t.ex ser att en funktion har ett k-värde på 3 och y = 4 när x = 5.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Då kan du räkna ut vad y-värdet är när x = 6 genom att ta 4+3*Δx= 4+3*1 = 7. Svar: y = 7 då x = 6", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -100)
    trtl.write("Om detta är svårt kan det vara bra att kolla lite extra på räta linjens ekvation.", font=('arial',15,'italic'), align='left')

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None

def funktio_tabell_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spel går ut på att bestämma räta linjens k-värde och m-värde (y = kx+m)", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("genom en värdetabell", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("K-värdet kan räknas ut genom att ta ∆y/∆x = k. (Triangeln står för delta, differensen av värdet).", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Välj två rader från tabellen. Ta sedan y-värdet från ena raden, subtraherat med den andra radens y-värde.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Dividera sedan skillnaden i y-värderna med (x-värdet från första rad subtraherat med den andra radens.)", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Ett exempel med värderna x1 = 2, y1 = 2 och x2 = 4, y2 = 8.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -100)
    trtl.write("Detta ger oss ∆y/∆x = (y2-y1)/(x2-x1) = (8-2)/(4-2) = 3. k = 3.", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -150)
    trtl.write("M-värdet är y-värdet när funktionen går genom y-axeln eller när x = 0. Eftersom y=k*0+m => y = m", font=('arial',15,'normal'), align='left')

    pos(trtl, -540, -200)
    trtl.write("Om inte tabellen visar vad y-värdet är när x = 0 får du räkna ut m-värdet själv. ", font=('arial',15,'italic'), align='left')
    pos(trtl, -540, -230)
    trtl.write("Gör detta genom att ta k-värdet multiplicerat ett x-värde i tabellen. Differensen mellan k*x och y-värdet ger dig m-värdet ", font=('arial',15,'italic'), align='left')

    trtl.ht()

    #Skärmen blir variablen "sc"    
    sc = turtle.Screen()
    user_guess = None

    #Tar in användarinput (klar)
    while user_guess == None:
        user_guess = (sc.textinput("Redo?", "Skriv klar:")) #obs här är det numera text
        if user_guess == "klar":
            trtl.clear()
            return
        else:
             time.sleep(0.5)
             user_guess = None