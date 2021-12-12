#Jennie
#Fel knapp 10gg gå vidare
import time
import random
import turtle

#Ger slumpade kordinater mellan -5 och 5
def kordinater():
    return (int(random.randint(-5, 5)))

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
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()

#Körs ifall användare fick fel
def wrong():
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()

#Kollar om användaren har samma svar som facit
def kolla(facitx, facity, trtl, scores):

    #Skälva skärmen läggs i variablen "sc"    
    sc = turtle.Screen()
    svarx = 0
    svary = 0

    #Tar in användarinput (svaren)
    while svary != None:
        try:
            svarx = (sc.textinput("Vad är x-kordinaten", "Ditt svar:")) #obs här är det numera text
            if svarx == "return":
                trtl.clear()
                return 
            svarx = int(svarx)#texten blir till siffra igen, om man skrev in annan text än return tar undantagshanteringen hand om det

            svary = (sc.textinput("Vad är y-kordinaten", "Ditt svar:")) #obs här är det numera text
            if svary == "return":
                trtl.clear()
                return 
            
            svary = int(svary)#texten blir till siffra igen, om man skrev in annan text än return tar undantagshanteringen hand om det

        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, 50, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            continue
        break

    #Skriver ut användarens svar
    pen(trtl, -240, 225, "black")
    trtl.write(f"Ditt svar: ({svarx}, {svary})",font=("Verdana", 12, "bold"))

    #Skriver ut rätt svar
    pen(trtl, -240, 207, "black")
    trtl.write(f"Rätt svar: ({facitx}, {facity})",font=("Verdana", 12, "bold"))

    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

    #Kollar ifall användaren hade rätt
    if facitx == svarx and facity == svary:
        scores["koordinater"]+=1 #Lägger till ett poäng i dict från main
        right(scores["koordinater"])#kör med globala poäng istället
    else:
        scores["koordinater"] = 0 #kör med globala poäng istället
        wrong()

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    padda(scores)

#Gör själva griden
def padda(scores):
    #Skapar sköldpadda + hastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)

    sc = turtle.Screen()

    sc.window_height()
    sc.window_width()

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

    #Tar in slumpmässigt x och y
    x = kordinater()
    y = kordinater()

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
    kolla(x, y, trtl, scores)
