#Jennie
import turtle
import random
import time

#Ger slumpade nummer mellan -10 och 10
def randomNumber():
    return (int(random.randint(-15, 15)))

#Ger slumpade nummer mellan -5 och 5
def randomNumber_nr2():
    return (int(random.randint(0, 5)))

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
    time.sleep(2)
    trtl.clear()

#Kollar om användaren har samma svar som facit
def kolla(facity, trtl, score):
    #Skälva skärmen läggs i variablen "sc"
    sc = turtle.Screen()
    svary = 0

    #Tar in användarinput (svaren)
    while svary != None:
        try:
            svary = float(sc.numinput("Vad är y?", "Ditt svar:"))
        except (TypeError, OverflowError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, -85, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            continue
        break

    pen(trtl, -240, 225, "black")
    trtl.write(f"Ditt svar: y = {svary}",font=("Verdana", 12, "bold"))

    pen(trtl, -240, 207, "black")
    trtl.write(f"Rätt svar: y = {facity}",font=("Verdana", 12, "bold"))

    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

    #Kollar ifall användaren hade rätt
    if facity == svary:
        score += 1
        newScore = right(score)
    else:
        wrong()
        newScore = score

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    grid(newScore)
    sc.exitonclick()

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
def ekvation_y(trtl, score):
    trtl.penup()

    c = randomNumber()
    a = randomNumber_nr2()
    x = randomNumber()
    y = c*x**a

    print(y)

    pen(trtl, -90, 30, "black")
    trtl.write(f"y = {c} * (x)^{a}",font=("Verdana", 12, "bold"))

    pen(trtl, -90, 0, "black")
    trtl.write(f"Vad är y om x = {x}",font=("Verdana", 12, "bold"))

    fyrkant(trtl)

    kolla(y, trtl, score)

#Gör själva ekvationen
def ekvation_x(trtl, score):
    trtl.penup()

    c = randomNumber()
    a = randomNumber_nr2()

    while a == 0:
            a = randomNumber_nr2()

    y = randomNumber()

    x = (y/c)**(1/a)

    print(x)


    pen(trtl, -90, 30, "black")
    trtl.write(f"y = {c} * (x)^{a}",font=("Verdana", 12, "bold"))

    pen(trtl, -90, 0, "black")
    trtl.write(f"Vad är x om y = {y}",font=("Verdana", 12, "bold"))

    fyrkant(trtl)

    kolla(x, trtl, score)

#Gör själva griden
def grid(score):
    #Skapar sköldpadda + hastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)
    
    #Skriver ut "y = C*a^x"
    pen(trtl, -50, -50, "black")
    trtl.write("y = Ca^x",font=("Verdana", 12, "bold"))

    #Gömmer sköldpadda
    trtl.hideturtle()

    # temp = int(random.randint(0, 1))

    temp = 0

    if temp == 1:
        ekvation_y(trtl, score)
    else:
        ekvation_x(trtl,score)

grid(0)