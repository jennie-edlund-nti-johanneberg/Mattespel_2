#Jennie
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

    # set position again
    trtl.penup()
    trtl.color("black")
    trtl.setpos(-240,225)
    trtl.pendown()
     
    #skriver användarens svar
    trtl.write(f"Ditt svar: ({int(svarx)}, {int(svary)})",font=("Verdana", 12, "bold"))

    # set position again
    trtl.penup()
    trtl.setpos(-240,207)
    trtl.pendown()

    #skriver rätt svar
    trtl.write(f"Rätt svar: ({facitx}, {facity})",font=("Verdana", 12, "bold"))

    time.sleep(3)

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
    sc.exitonclick()

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

    # set position again
    trtl.penup()
    trtl.setpos(246,-8)
    trtl.pendown()

    trtl.write(">", font=("Verdana", 12, "bold"))

    trtl.pu()
    trtl.setx(-250)
    trtl.sety(0)
    trtl.rt(90)
    trtl.pd() 
    trtl.fd(500)

    trtl.penup()
    trtl.setpos(-6,240)
    trtl.pendown()

    trtl.write("^", font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(235,0)
    trtl.pendown()
     
    # write x
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(5,235)
    trtl.pendown()
     
    # write y
    trtl.write("y",font=("Verdana", 12, "bold"))

         
    # set position again
    trtl.penup()
    trtl.setpos(5,43)
    trtl.pendown()
     
    # write 1
    trtl.write("1",font=("Verdana", 12, "bold"))

    # set position again
    trtl.penup()
    trtl.setpos(46,5)
    trtl.pendown()
     
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