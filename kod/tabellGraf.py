#Jennie
import turtle
import random
import time

def randomNumber():
    return (int(random.randint(-3, 3)))

def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

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

def kolla(facitk, facitm, trtl, score):
    sc = turtle.Screen()
    
    x = randomNumber()
    facity = facitk*x+facitm
    #sc_2 = sc.setup(600, 300)
    svary = (sc.numinput(f"Vad är y när x = {x}", "Ditt svar:"))

    # set position again
    pen(trtl, -240, 225, "black")

    #skriver användarens svar
    trtl.write(f"Ditt svar: y = {int(svary)}",font=("Verdana", 12, "bold"))

    # set position again
    pen(trtl, -240, 207, "black")

    #skriver rätt svar
    trtl.write(f"Rätt svar: y = {facity}",font=("Verdana", 12, "bold"))

    trtl.hideturtle()
    time.sleep(3)

    if facity == svary:
        score += 1
        newScore = right(score)
        #print("rätt")
    else:
        wrong()
        newScore = score
        #print("nej")
    trtl.clear()
    grid(newScore)
    sc.exitonclick()

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

def grid(score):
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
    
    # set position again

    pen(trtl, -240, -235, "black")
     
    # write y = kx+m
    trtl.write("y = kx+m",font=("Verdana", 12, "bold"))


    trtl.setheading(0)

    plotter(trtl, range(-240, 240), score)


    trtl.hideturtle()

    turtle.done()

grid(0)