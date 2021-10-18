#Jennie
import turtle
import random
import time

def kolla(facitk, facitm, trtl, score):
    sc = turtle.Screen()
    svark = (sc.numinput("Vad är k-konstanten", "Ditt svar:"))
    svarm = (sc.numinput("Vad är m-konstanten", "Ditt svar:"))

    # set position again
    trtl.penup()
    trtl.color("black")
    trtl.setpos(-240,225)
    trtl.pendown()

    #skriver användarens svar
    if svarm < 0:
        trtl.write(f"Ditt svar: y = {int(svark)}x{int(svarm)}",font=("Verdana", 12, "bold"))
    elif svarm > 0:
        trtl.write(f"Ditt svar: y = {int(svark)}x+{int(svarm)}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Ditt svar: y = {int(svark)}x",font=("Verdana", 12, "bold"))

    # if svark == 0:
    #     trtl.write(f"Ditt svar: y = x+{int(svarm)}",font=("Verdana", 12, "bold"))
    

    # set position again
    trtl.penup()
    trtl.setpos(-240,207)
    trtl.pendown()

    #skriver rätt svar
    if facitm < 0:
        trtl.write(f"Rätt svar: y = {facitk}x{facitm}",font=("Verdana", 12, "bold"))
    elif facitm > 0:
        trtl.write(f"Rätt svar: y = {facitk}x+{facitm}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Rätt svar: y = {facitk}x",font=("Verdana", 12, "bold"))

    # if facitk == 0:
    #     trtl.write(f"Ditt svar: y = x+{int(facitm)}",font=("Verdana", 12, "bold"))

    trtl.hideturtle()
    time.sleep(3)

    if facitk == svark and facitm == svarm:
        score += 1
        newScore = right(score)
        #print("rätt")
    else:
        wrong()
        newScore = score
        #print("nej")
    trtl.clear()
    grid(newScore)

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

def grid(score):
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
    
    # set position again
    trtl.penup()
    trtl.setpos(-240,-235)
    trtl.pendown()
     
    # write y = kx+m
    trtl.write("y = kx+m",font=("Verdana", 12, "bold"))


    trtl.setheading(0)

    plotter(trtl, range(-240, 240), score)


    trtl.hideturtle()

    turtle.done()


def randomNumber():
    return (int(random.randint(-5, 5)))

def plotter(trtl, x_range, score):
    trtl.penup()

    k = randomNumber()
    m = randomNumber()
    #print(f"k: {k}")
    #print(f"m: {m}")

    for x in x_range:
        y = (k*x + m*50)
        trtl.goto(x, y)
        trtl.pendown()

    kolla(k, m, trtl, score)


grid(0)