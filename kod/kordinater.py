#Jennie
import time
import random
import turtle

#Ger slumpade kordinater
def kordinater():
    return (int(random.randint(-5, 5)))

#Ger turtle position och färg
def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

#Ifall användare fick rätt
def right(score):
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

#Ifall användare fick fel
def wrong():
    trtl = turtle.Turtle()
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()

#Kollar om användaren har rätt
def kolla(facitx, facity, trtl, score):
    sc = turtle.Screen()
    svarx = (sc.numinput("Vad är x-kordinaten", "Ditt svar:"))
    svary = (sc.numinput("Vad är y-kordinaten", "Ditt svar:"))

    # set position again
    pen(trtl, -240, 225, "black")

    #skriver användarens svar
    trtl.write(f"Ditt svar: ({int(svarx)}, {int(svary)})",font=("Verdana", 12, "bold"))

    pen(trtl, -240, 207, "black")

    #skriver rätt svar
    trtl.write(f"Rätt svar: ({facitx}, {facity})",font=("Verdana", 12, "bold"))

    time.sleep(3)

    if facitx == svarx and facity == svary:
        score += 1
        newScore = right(score)
    else:
        wrong()
        newScore = score
    trtl.clear()
    padda(newScore)
    sc.exitonclick()

def padda(score):

    trtl = turtle.Turtle()

    trtl.speed(0)

    for i in range(11):
        pen(trtl, -250, 250-(50*i), "lightgrey")
        trtl.fd(500)

    trtl.lt(90)

    for i in range(11):
        pen(trtl, 250-(50*i), -250, "lightgrey")        
        trtl.fd(500)


    pen(trtl, 0, -250, "black")     
    trtl.fd(500)

    # set position again
    pen(trtl, 246, -8, "black")    

    trtl.write(">", font=("Verdana", 12, "bold"))

    pen(trtl, -250, 0, "black")
    trtl.rt(90)
    trtl.fd(500)

    pen(trtl, -6, 240, "black")

    trtl.write("^", font=("Verdana", 12, "bold"))

    # set position again
    pen(trtl, 235, 0, "black")

    # write x
    trtl.write("x",font=("Verdana", 12, "bold"))

    # set position again
    pen(trtl, 5, 235, "black")

    # write y
    trtl.write("y",font=("Verdana", 12, "bold"))


    # set position again
    pen(trtl, 5, 43, "black")

    # write 1
    trtl.write("1",font=("Verdana", 12, "bold"))

    # set position again
    pen(trtl, 46, 5, "black")

    # write 1
    trtl.write("1",font=("Verdana", 12, "bold"))


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