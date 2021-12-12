#Jennie
import turtle
import random
import time

#Ger slumpade nummer mellan -5 och 5
def randomNumber():
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
    time.sleep(2)
    trtl.clear()

#Kollar om användaren har samma svar som facit
def kolla(facitk, facitm, trtl, scores):
    #Skälva skärmen läggs i variablen "sc"
    sc = turtle.Screen()
    svark = None
    svarm = None
    #Tar in användarinput (svaren)
    while svark == None:
        try:
            svark = (sc.textinput("Vad är k-konstanten", "Ditt svar:"))
            if svark == "return":
                trtl.clear()
                return 
            svark = int(svark)
            
            svarm = (sc.textinput("Vad är m-konstanten", "Ditt svar:")) #obs här är det numera text
            if svarm == "return":
                trtl.clear()
                return 
            svarm = int(svarm)
        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, 50, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            svark = None
        

    #Skriver ut användarens svar
    pen(trtl, -240, 225, "black")
    if svarm < 0:
        trtl.write(f"Ditt svar: y = {svark}x{int(svarm)}",font=("Verdana", 12, "bold"))
    elif svarm > 0:
        trtl.write(f"Ditt svar: y = {svark}x+{int(svarm)}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Ditt svar: y = {svark}x",font=("Verdana", 12, "bold"))
    

    #Skriver ut rätt svar
    pen(trtl, -240, 207, "black")
    if facitm < 0:
        trtl.write(f"Rätt svar: y = {facitk}x{facitm}",font=("Verdana", 12, "bold"))
    elif facitm > 0:
        trtl.write(f"Rätt svar: y = {facitk}x+{facitm}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Rätt svar: y = {facitk}x",font=("Verdana", 12, "bold"))

    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

    #Kollar ifall användaren hade rätt
    if facitk == svark and facitm == svarm:
        scores["givengraf"] += 1
        right(scores["givengraf"])
    else:
        scores["givengraf"] = 0
        wrong()

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    grid(scores)

#Plottar själva grafen
def plotter(trtl, x_range, scores):
    trtl.penup()

    k = randomNumber()
    m = randomNumber()

    for x in x_range:
        y = (k*x + m*50)
        trtl.goto(x, y)
        trtl.color("red")
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